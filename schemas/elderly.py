# -*- coding: utf-8 -*-
"""老人全维档案模型 — 所有Agent的数据入口"""

from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class Gender(str, Enum):
    MALE = "男"
    FEMALE = "女"


class CareSetting(str, Enum):
    HOME = "居家"
    COMMUNITY = "社区日间照料"
    INSTITUTION = "机构养老"


class Diagnosis(BaseModel):
    name: str = Field(..., description="疾病名称")
    diagnosed_year: Optional[int] = Field(None, description="确诊年份")
    control_status: Optional[str] = Field("尚可", description="控制状态: 良好/尚可/欠佳/未控制")
    notes: Optional[str] = Field(None, description="备注")


class Medication(BaseModel):
    name: str = Field(..., description="药品通用名")
    dosage: str = Field(..., description="剂量，如 '5mg qd'")
    indication: str = Field(..., description="适应症")
    start_date: Optional[str] = Field(None, description="开始用药日期")


class VitalSigns(BaseModel):
    systolic_bp: Optional[int] = Field(None, description="收缩压 mmHg")
    diastolic_bp: Optional[int] = Field(None, description="舒张压 mmHg")
    heart_rate: Optional[int] = Field(None, description="心率 bpm")
    fasting_glucose: Optional[float] = Field(None, description="空腹血糖 mmol/L")
    hba1c: Optional[float] = Field(None, description="糖化血红蛋白 %")
    spo2: Optional[int] = Field(None, description="血氧饱和度 %")
    temperature: Optional[float] = Field(None, description="体温 ℃")


class LabResults(BaseModel):
    albumin: Optional[float] = Field(None, description="白蛋白 g/L")
    hemoglobin: Optional[float] = Field(None, description="血红蛋白 g/L")
    creatinine: Optional[float] = Field(None, description="肌酐 μmol/L")
    egfr: Optional[float] = Field(None, description="eGFR ml/min/1.73m²")
    potassium: Optional[float] = Field(None, description="血钾 mmol/L")
    uric_acid: Optional[float] = Field(None, description="尿酸 μmol/L")


class ADLScores(BaseModel):
    """Barthel指数各子项"""
    feeding: int = Field(10, ge=0, le=10, description="进食")
    bathing: int = Field(5, ge=0, le=5, description="洗澡")
    grooming: int = Field(5, ge=0, le=5, description="修饰")
    dressing: int = Field(10, ge=0, le=10, description="穿衣")
    bowels: int = Field(10, ge=0, le=10, description="大便控制")
    bladder: int = Field(10, ge=0, le=10, description="小便控制")
    toilet_use: int = Field(10, ge=0, le=10, description="如厕")
    transfers: int = Field(15, ge=0, le=15, description="床椅转移")
    mobility: int = Field(15, ge=0, le=15, description="平地行走")
    stairs: int = Field(10, ge=0, le=10, description="上下楼梯")

    @property
    def total(self) -> int:
        return sum([
            self.feeding, self.bathing, self.grooming, self.dressing,
            self.bowels, self.bladder, self.toilet_use, self.transfers,
            self.mobility, self.stairs
        ])


class ElderlyProfile(BaseModel):
    """老人全维档案"""
    # 基本信息
    name: str = Field(..., description="姓名")
    age: int = Field(..., ge=60, le=120, description="年龄")
    gender: Gender = Field(..., description="性别")
    care_setting: CareSetting = Field(..., description="照护场景")
    days_in_care: Optional[int] = Field(None, description="已入住天数(机构)")

    # 医疗维度
    diagnoses: list[Diagnosis] = Field(default_factory=list, description="疾病诊断列表")
    medications: list[Medication] = Field(default_factory=list, description="用药列表")
    vitals: Optional[VitalSigns] = Field(None, description="生命体征")
    labs: Optional[LabResults] = Field(None, description="化验结果")
    allergies: list[str] = Field(default_factory=list, description="过敏史")
    fall_history: Optional[str] = Field(None, description="跌倒史描述")

    # 护理维度
    adl_scores: Optional[ADLScores] = Field(None, description="Barthel ADL评分")
    morse_score: Optional[int] = Field(None, ge=0, le=125, description="Morse跌倒评估")
    braden_score: Optional[int] = Field(None, ge=6, le=23, description="Braden压疮评估")
    mobility_note: Optional[str] = Field(None, description="行动能力描述")
    has_catheter: bool = Field(False, description="是否留置导尿")
    has_ng_tube: bool = Field(False, description="是否留置鼻饲管")

    # 社工维度
    gds_score: Optional[int] = Field(None, ge=0, le=15, description="GDS-15老年抑郁量表")
    mmse_score: Optional[int] = Field(None, ge=0, le=30, description="MMSE认知评分")
    social_activities: Optional[str] = Field(None, description="社会活动参与描述")
    family_visit_frequency: Optional[str] = Field(None, description="家属探视频率")
    family_relationship: Optional[str] = Field(None, description="家庭关系评估")
    life_story: Optional[str] = Field(None, description="生活史关键事件")

    # 餐饮维度
    height_cm: Optional[float] = Field(None, description="身高 cm")
    weight_kg: Optional[float] = Field(None, description="体重 kg")
    weight_change_1m: Optional[float] = Field(None, description="近1月体重变化 kg")
    swallowing_test: Optional[str] = Field(None, description="洼田饮水试验等级 (1-5级)")
    dental_status: Optional[str] = Field(None, description="牙齿状况")
    dietary_restrictions: list[str] = Field(default_factory=list, description="饮食医嘱限制")

    @property
    def bmi(self) -> Optional[float]:
        if self.height_cm and self.weight_kg:
            return round(self.weight_kg / (self.height_cm / 100) ** 2, 1)
        return None

    @property
    def adl_total(self) -> Optional[int]:
        if self.adl_scores:
            return self.adl_scores.total
        return None

    @property
    def care_level_label(self) -> str:
        """根据ADL总分判定照护等级"""
        if self.adl_total is None:
            return "未评估"
        if self.adl_total <= 20:
            return "重度依赖(一级照护)"
        elif self.adl_total <= 40:
            return "重度依赖(二级照护)"
        elif self.adl_total <= 60:
            return "中度依赖(三级照护)"
        elif self.adl_total <= 99:
            return "轻度依赖"
        else:
            return "自理"
