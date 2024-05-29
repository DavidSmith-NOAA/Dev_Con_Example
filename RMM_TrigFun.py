# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 21:10:08 2022

@author: JLisonbee
"""
import numpy as np
import pandas as pd


file = 'RMM_TrigFun.xlsx'
MJO = pd.read_excel(file)
RMM1 = MJO.RMM1
RMM2 = MJO.RMM2

Angle = np.arctan(RMM2/RMM1)*180/np.pi
MJO['Angle']=Angle
Angle[Angle < 0] = Angle[Angle < 0]+360
Calc_amp = np.sqrt(RMM1**2+RMM2**2)
Calc_phase = np.zeros(len(Angle))

Calc_phase[Angle.between(0,45)] = 5
Calc_phase[Angle.between(45,90)] = 6
Calc_phase[Angle.between(90,135)] = 7
Calc_phase[Angle.between(135,180)] = 8
Calc_phase[Angle.between(180,225)] = 1
Calc_phase[Angle.between(225,270)] = 2
Calc_phase[Angle.between(270,315)] = 3
Calc_phase[Angle.between(315,360)] = 4

MJO['Calc_amplitude'] = Calc_amp
MJO['Calc_phase'] = Calc_phase

    
