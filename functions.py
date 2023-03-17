def show_window_2(self):
    self.w2 = SecondWindow()
    self.load_second_window()
    self.load_visual_window()
    self.w2.show()

def load_second_window(self):
    self.red_style = '''
    QLabel{
        color: rgb(156, 0, 6);
        background-color: rgb(255, 199, 206);
    }
    '''
    self.green_style = '''
    QLabel{
        color: rgb(0, 97, 0);
        background-color: rgb(198, 239, 206);
    }
    '''
    #текущая ликвидность
    self.w2.label_1_0.setText(str(self.stats.current_liquidity()))
    self.w2.label_1_1.setText(str(self.stats.current_liquidity(period=1)))
    self.w2.label_1_2.setText(str(self.stats.current_liquidity(period=2)))
    self.w2.label_1_3.setText(str(self.stats.current_liquidity(period=3)))
    if 1.0 < self.stats.current_liquidity(period=0) < 2.0:
        self.w2.label_1_0.setStyleSheet(self.green_style)
    else:
        self.w2.label_1_0.setStyleSheet(self.red_style)
    if 1.0 < self.stats.current_liquidity(period=1) < 2.0:
        self.w2.label_1_1.setStyleSheet(self.green_style)
    else:
        self.w2.label_1_1.setStyleSheet(self.red_style)
    if 1.0 < self.stats.current_liquidity(period=2) < 2.0:
        self.w2.label_1_2.setStyleSheet(self.green_style)
    else:
        self.w2.label_1_2.setStyleSheet(self.red_style)
    if 1.0 < self.stats.current_liquidity(period=3) < 2.0:
        self.w2.label_1_3.setStyleSheet(self.green_style)
    else:
        self.w2.label_1_3.setStyleSheet(self.red_style)
    #быстрая ликвидность
    self.w2.label_2_0.setText(str(self.stats.fast_liquidity()))
    self.w2.label_2_1.setText(str(self.stats.fast_liquidity(period=1)))
    self.w2.label_2_2.setText(str(self.stats.fast_liquidity(period=2)))
    self.w2.label_2_3.setText(str(self.stats.fast_liquidity(period=3)))
    if 0.7 < self.stats.fast_liquidity() < 1.0:
        self.w2.label_2_0.setStyleSheet(self.green_style)
    else:
        self.w2.label_2_0.setStyleSheet(self.red_style)
    if 0.7 < self.stats.fast_liquidity(period=1) < 1.0:
        self.w2.label_2_1.setStyleSheet(self.green_style)
    else:
        self.w2.label_2_1.setStyleSheet(self.red_style)
    if 0.7 < self.stats.fast_liquidity(period=2) < 1.0:
        self.w2.label_2_2.setStyleSheet(self.green_style)
    else:
        self.w2.label_2_2.setStyleSheet(self.red_style)
    if 0.7 < self.stats.fast_liquidity(period=3) < 1.0:
        self.w2.label_2_3.setStyleSheet(self.green_style)
    else:
        self.w2.label_2_3.setStyleSheet(self.red_style)
    #абсолютная ликвидность
    self.w2.label_3_0.setText(str(self.stats.absolute_liquidity()))
    self.w2.label_3_1.setText(str(self.stats.absolute_liquidity(period=1)))
    self.w2.label_3_2.setText(str(self.stats.absolute_liquidity(period=2)))
    self.w2.label_3_3.setText(str(self.stats.absolute_liquidity(period=3)))
    if 0.2 < self.stats.absolute_liquidity() < 0.5:
        self.w2.label_3_0.setStyleSheet(self.green_style)
    else:
        self.w2.label_3_0.setStyleSheet(self.red_style)
    if 0.2 < self.stats.absolute_liquidity(period=1) < 0.5:
        self.w2.label_3_1.setStyleSheet(self.green_style)
    else:
        self.w2.label_3_1.setStyleSheet(self.red_style)
    if 0.2 < self.stats.absolute_liquidity(period=2) < 0.5:
        self.w2.label_3_2.setStyleSheet(self.green_style)
    else:
        self.w2.label_3_2.setStyleSheet(self.red_style)
    if 0.2 < self.stats.absolute_liquidity(period=3) < 0.5:
        self.w2.label_3_3.setStyleSheet(self.green_style)
    else:
        self.w2.label_3_3.setStyleSheet(self.red_style)
    #финансовая независимость
    self.w2.label_4_0.setText(str(self.stats.financial_independence()))
    self.w2.label_4_1.setText(str(self.stats.financial_independence(period=1)))
    self.w2.label_4_2.setText(str(self.stats.financial_independence(period=2)))
    self.w2.label_4_3.setText(str(self.stats.financial_independence(period=3)))
    if 0.4 < self.stats.financial_independence() < 0.6:
        self.w2.label_4_0.setStyleSheet(self.green_style)
    else:
        self.w2.label_4_0.setStyleSheet(self.red_style)
    if 0.4 < self.stats.financial_independence(period=1) < 0.6:
        self.w2.label_4_1.setStyleSheet(self.green_style)
    else:
        self.w2.label_4_1.setStyleSheet(self.red_style)
    if 0.4 < self.stats.financial_independence(period=2) < 0.6:
        self.w2.label_4_2.setStyleSheet(self.green_style)
    else:
        self.w2.label_4_2.setStyleSheet(self.red_style)
    if 0.4 < self.stats.financial_independence(period=3) < 0.6:
        self.w2.label_4_3.setStyleSheet(self.green_style)
    else:
        self.w2.label_4_3.setStyleSheet(self.red_style)
    #финансовый рычаг
    self.w2.label_5_0.setText(str(self.stats.leverage_ratio()))
    self.w2.label_5_1.setText(str(self.stats.leverage_ratio(period=1)))
    self.w2.label_5_2.setText(str(self.stats.leverage_ratio(period=2)))
    self.w2.label_5_3.setText(str(self.stats.leverage_ratio(period=3)))
    if 0 < self.stats.leverage_ratio() < 1.5:
        self.w2.label_5_0.setStyleSheet(self.green_style)
    else:
        self.w2.label_5_0.setStyleSheet(self.red_style)
    if 0 < self.stats.leverage_ratio(period=1) < 1.5:
        self.w2.label_5_1.setStyleSheet(self.green_style)
    else:
        self.w2.label_5_1.setStyleSheet(self.red_style)
    if 0 < self.stats.leverage_ratio(period=2) < 1.5:
        self.w2.label_5_2.setStyleSheet(self.green_style)
    else:
        self.w2.label_5_2.setStyleSheet(self.red_style)
    if 0 < self.stats.leverage_ratio(period=3) < 1.5:
        self.w2.label_5_3.setStyleSheet(self.green_style)
    else:
        self.w2.label_5_3.setStyleSheet(self.red_style)
    #обеспеченность СОС
    self.w2.label_6_0.setText(str(self.stats.own_working_capital()))
    self.w2.label_6_1.setText(str(self.stats.own_working_capital(period=1)))
    self.w2.label_6_2.setText(str(self.stats.own_working_capital(period=2)))
    self.w2.label_6_3.setText(str(self.stats.own_working_capital(period=3)))
    if self.stats.own_working_capital() > 0.1:
        self.w2.label_6_0.setStyleSheet(self.green_style)
    else:
        self.w2.label_6_0.setStyleSheet(self.red_style)
    if self.stats.own_working_capital(period=1) > 0.1:
        self.w2.label_6_1.setStyleSheet(self.green_style)
    else:
        self.w2.label_6_1.setStyleSheet(self.red_style)
    if self.stats.own_working_capital(period=2) > 0.1:
        self.w2.label_6_2.setStyleSheet(self.green_style)
    else:
        self.w2.label_6_2.setStyleSheet(self.red_style)
    if self.stats.own_working_capital(period=3) > 0.1:
        self.w2.label_6_3.setStyleSheet(self.green_style)
    else:
        self.w2.label_6_3.setStyleSheet(self.red_style)
    #период оборота запасов
    self.w2.label_7_0.setText(str(self.stats.inventory_turnover_period()))
    self.w2.label_7_1.setText(str(self.stats.inventory_turnover_period(period=1)))
    self.w2.label_7_2.setText(str(self.stats.inventory_turnover_period(period=2)))
    self.w2.label_7_3.setText(str(self.stats.inventory_turnover_period(period=3)))
    # коэффициент оборачиваемости запасов
    self.w2.label_8_0.setText(str(self.stats.inventory_turnover_ratio()))
    self.w2.label_8_1.setText(str(self.stats.inventory_turnover_ratio(period=1)))
    self.w2.label_8_2.setText(str(self.stats.inventory_turnover_ratio(period=2)))
    self.w2.label_8_3.setText(str(self.stats.inventory_turnover_ratio(period=3)))
    #период оборота дебиторской задолженности
    self.w2.label_9_0.setText(str(self.stats.accounts_receivable_turnover_period()))
    self.w2.label_9_1.setText(str(self.stats.accounts_receivable_turnover_period(period=1)))
    self.w2.label_9_2.setText(str(self.stats.accounts_receivable_turnover_period(period=2)))
    self.w2.label_9_3.setText(str(self.stats.accounts_receivable_turnover_period(period=3)))
    #коэффициент оборачиваемости дебиторской задолженности
    self.w2.label_10_0.setText(str(self.stats.accounts_receivable_turnover_ratio()))
    self.w2.label_10_1.setText(str(self.stats.accounts_receivable_turnover_ratio(period=1)))
    self.w2.label_10_2.setText(str(self.stats.accounts_receivable_turnover_ratio(period=2)))
    self.w2.label_10_3.setText(str(self.stats.accounts_receivable_turnover_ratio(period=3)))
    # период оборота кредиторской задолженности
    self.w2.label_11_0.setText(str(self.stats.accounts_payable_turnover_period()))
    self.w2.label_11_1.setText(str(self.stats.accounts_payable_turnover_period(period=1)))
    self.w2.label_11_2.setText(str(self.stats.accounts_payable_turnover_period(period=2)))
    self.w2.label_11_3.setText(str(self.stats.accounts_payable_turnover_period(period=3)))
    # коэффициент оборачиваемости кредиторской задолженности
    self.w2.label_12_0.setText(str(self.stats.accounts_payable_turnover_ratio()))
    self.w2.label_12_1.setText(str(self.stats.accounts_payable_turnover_ratio(period=1)))
    self.w2.label_12_2.setText(str(self.stats.accounts_payable_turnover_ratio(period=2)))
    self.w2.label_12_3.setText(str(self.stats.accounts_payable_turnover_ratio(period=3)))
    #операционный цикл
    self.w2.label_13_0.setText(str(self.stats.operating_cycle()))
    self.w2.label_13_1.setText(str(self.stats.operating_cycle(period=1)))
    self.w2.label_13_2.setText(str(self.stats.operating_cycle(period=2)))
    self.w2.label_13_3.setText(str(self.stats.operating_cycle(period=3)))
    # финансовый цикл
    self.w2.label_14_0.setText(str(self.stats.financial_cycle()))
    self.w2.label_14_1.setText(str(self.stats.financial_cycle(period=1)))
    self.w2.label_14_2.setText(str(self.stats.financial_cycle(period=2)))
    self.w2.label_14_3.setText(str(self.stats.financial_cycle(period=3)))
    #рентабельность активов
    self.w2.label_15_0.setText(str(self.stats.return_on_assets()))
    self.w2.label_15_1.setText(str(self.stats.return_on_assets(period=1)))
    self.w2.label_15_2.setText(str(self.stats.return_on_assets(period=2)))
    self.w2.label_15_3.setText(str(self.stats.return_on_assets(period=3)))
    #рентабельность собственного капитала
    self.w2.label_16_0.setText(str(self.stats.return_on_equity()))
    self.w2.label_16_1.setText(str(self.stats.return_on_equity(period=1)))
    self.w2.label_16_2.setText(str(self.stats.return_on_equity(period=2)))
    self.w2.label_16_3.setText(str(self.stats.return_on_equity(period=3)))
    #рентабельность прибыли от продаж
    self.w2.label_17_0.setText(str(self.stats.return_on_profit_from_sales()))
    self.w2.label_17_1.setText(str(self.stats.return_on_profit_from_sales(period=1)))
    self.w2.label_17_2.setText(str(self.stats.return_on_profit_from_sales(period=2)))
    self.w2.label_17_3.setText(str(self.stats.return_on_profit_from_sales(period=3)))
    #маржа чистой прибыли
    self.w2.label_18_0.setText(str(self.stats.net_profit_margin()))
    self.w2.label_18_1.setText(str(self.stats.net_profit_margin(period=1)))
    self.w2.label_18_2.setText(str(self.stats.net_profit_margin(period=2)))
    self.w2.label_18_3.setText(str(self.stats.net_profit_margin(period=3)))
def load_visual_window(self):
    self.w2.label_print_0_1.setText(str(self.stats.vis_cur_liq()))
    self.w2.label_print_0_2.setText(str(self.stats.vis_fast_liq()))
    self.w2.label_print_0_3.setText(str(self.stats.vis_abs_liq()))
    self.w2.label_print_0_4.setText(str(self.stats.vis_fin_ind()))
    self.w2.label_print_0_5.setText(str(self.stats.vis_lev_rat()))
    self.w2.label_print_0_6.setText(str(self.stats.vis_work_cap()))
    self.w2.label_print_0_7.setText(str(self.stats.vis_inv_per()))
    self.w2.label_print_0_8.setText(str(self.stats.vis_inv_rat()))
    self.w2.label_print_0_9.setText(str(self.stats.vis_rec_per()))
    self.w2.label_print_0_10.setText(str(self.stats.vis_rec_rat()))
    self.w2.label_print_0_11.setText(str(self.stats.vis_pay_per()))
    self.w2.label_print_0_12.setText(str(self.stats.vis_pay_rat()))
    self.w2.label_print_0_13.setText(str(self.stats.vis_oper_cyc()))
    self.w2.label_print_0_14.setText(str(self.stats.vis_fin_cyc()))
    self.w2.label_print_0_15.setText(str(self.stats.vis_roa()))
    self.w2.label_print_0_16.setText(str(self.stats.vis_roe()))
    self.w2.label_print_0_17.setText(str(self.stats.vis_ropfs()))
    self.w2.label_print_0_18.setText(str(self.stats.vis_net_mar()))
def random_button(self):
    self.randomize(period=0)
    self.randomize(period=1)
    self.randomize(period=2)
    self.randomize(period=3)
def randomize(self, period):
    #находим случайные числа для III, IV, V разделов
    self.C = randint(100000, 1000000)
    self.D = randint(100000, 1000000)
    self.E = randint(100000, 1000000)
    print('Раздел III =', self.C)
    print('Раздел IV =', self.D)
    print('Раздел V =', self.E)
    #находим валюту баланса
    self.total = self.C + self.D + self.E
    print(self.total)
    #создаем список весов для I/II разделов
    self.weights_active = [x/100 for x in range(35, 66)]
    print(self.weights_active)
    #находим размер I раздела
    self.A = self.total * choice(self.weights_active)
    self.B = self.total - self.A
    self.w_1 = [0.15, 0.13, 0.11, 0.07, 0.03, 0.01, 0]
    shuffle(self.w_1)
    self.w_2 = [0.36, 0.03, 0.30, 0.15, 0.14, 0.02]
    shuffle(self.w_2)
    self.w_3 = [0.01, 0.02, 0.02, 0]
    shuffle(self.w_3)
    self.w_4 = [0.88, 0.10, 0.02, 0]
    shuffle(self.w_4)
    self.w_5 = [0.18, 0.72, 0.07, 0, 0.03]
    shuffle(self.w_5)
    #актив
    # period_0
    if period == 0:
        self.horizontalSlider_0_1110.setMaximum(trunc(self.A))
        self.horizontalSlider_0_1120.setMaximum(trunc(self.A))
        self.horizontalSlider_0_1130.setMaximum(trunc(self.A))
        self.horizontalSlider_0_1140.setMaximum(trunc(self.A))
        self.horizontalSlider_0_1150.setMaximum(trunc(self.A))
        self.horizontalSlider_0_1160.setMaximum(trunc(self.A))
        self.horizontalSlider_0_1170.setMaximum(trunc(self.A))
        self.horizontalSlider_0_1180.setMaximum(trunc(self.A))
        self.horizontalSlider_0_1190.setMaximum(trunc(self.A))
        self.horizontalSlider_0_1100.setMaximum(trunc(self.total))
        self.horizontalSlider_0_1110.setValue(trunc(self.A * self.w_1[0]))
        self.horizontalSlider_0_1120.setValue(trunc(self.A * self.w_1[1]))
        self.horizontalSlider_0_1130.setValue(trunc(self.A * self.w_1[2]))
        self.horizontalSlider_0_1140.setValue(trunc(self.A * self.w_1[3]))
        self.horizontalSlider_0_1150.setValue(trunc(self.A * 0.4))
        self.horizontalSlider_0_1160.setValue(trunc(self.A * self.w_1[4]))
        self.horizontalSlider_0_1170.setValue(trunc(self.A * 0.2))
        self.horizontalSlider_0_1180.setValue(trunc(self.A * self.w_1[5]))
        self.horizontalSlider_0_1190.setValue(trunc(self.A * self.w_1[6]))
        self.horizontalSlider_0_1100.setValue(trunc(self.A))
        self.horizontalSlider_0_1210.setMaximum(trunc(self.B))
        self.horizontalSlider_0_1220.setMaximum(trunc(self.B))
        self.horizontalSlider_0_1230.setMaximum(trunc(self.B))
        self.horizontalSlider_0_1240.setMaximum(trunc(self.B))
        self.horizontalSlider_0_1250.setMaximum(trunc(self.B))
        self.horizontalSlider_0_1260.setMaximum(trunc(self.B))
        self.horizontalSlider_0_1200.setMaximum(trunc(self.total))
        self.horizontalSlider_0_1600.setMaximum(trunc(self.total))
        self.horizontalSlider_0_1210.setValue(trunc(self.B * self.w_2[0]))
        self.horizontalSlider_0_1220.setValue(trunc(self.B * self.w_2[1]))
        self.horizontalSlider_0_1230.setValue(trunc(self.B * self.w_2[2]))
        self.horizontalSlider_0_1240.setValue(trunc(self.B * self.w_2[3]))
        self.horizontalSlider_0_1250.setValue(trunc(self.B * self.w_2[4]))
        self.horizontalSlider_0_1260.setValue(trunc(self.B * self.w_2[5]))
        self.horizontalSlider_0_1200.setValue(trunc(self.B))
        self.horizontalSlider_0_1600.setValue(trunc(self.total))
    # period_1
    if period == 1:
        self.horizontalSlider_1_1110.setMaximum(trunc(self.A))
        self.horizontalSlider_1_1120.setMaximum(trunc(self.A))
        self.horizontalSlider_1_1130.setMaximum(trunc(self.A))
        self.horizontalSlider_1_1140.setMaximum(trunc(self.A))
        self.horizontalSlider_1_1150.setMaximum(trunc(self.A))
        self.horizontalSlider_1_1160.setMaximum(trunc(self.A))
        self.horizontalSlider_1_1170.setMaximum(trunc(self.A))
        self.horizontalSlider_1_1180.setMaximum(trunc(self.A))
        self.horizontalSlider_1_1190.setMaximum(trunc(self.A))
        self.horizontalSlider_1_1100.setMaximum(trunc(self.total))
        self.horizontalSlider_1_1110.setValue(trunc(self.A * self.w_1[0]))
        self.horizontalSlider_1_1120.setValue(trunc(self.A * self.w_1[1]))
        self.horizontalSlider_1_1130.setValue(trunc(self.A * self.w_1[2]))
        self.horizontalSlider_1_1140.setValue(trunc(self.A * self.w_1[3]))
        self.horizontalSlider_1_1150.setValue(trunc(self.A * 0.4))
        self.horizontalSlider_1_1160.setValue(trunc(self.A * self.w_1[4]))
        self.horizontalSlider_1_1170.setValue(trunc(self.A * 0.2))
        self.horizontalSlider_1_1180.setValue(trunc(self.A * self.w_1[5]))
        self.horizontalSlider_1_1190.setValue(trunc(self.A * self.w_1[6]))
        self.horizontalSlider_1_1100.setValue(trunc(self.A))
        self.horizontalSlider_1_1210.setMaximum(trunc(self.B))
        self.horizontalSlider_1_1220.setMaximum(trunc(self.B))
        self.horizontalSlider_1_1230.setMaximum(trunc(self.B))
        self.horizontalSlider_1_1240.setMaximum(trunc(self.B))
        self.horizontalSlider_1_1250.setMaximum(trunc(self.B))
        self.horizontalSlider_1_1260.setMaximum(trunc(self.B))
        self.horizontalSlider_1_1200.setMaximum(trunc(self.total))
        self.horizontalSlider_1_1600.setMaximum(trunc(self.total))
        self.horizontalSlider_1_1210.setValue(trunc(self.B * self.w_2[0]))
        self.horizontalSlider_1_1220.setValue(trunc(self.B * self.w_2[1]))
        self.horizontalSlider_1_1230.setValue(trunc(self.B * self.w_2[2]))
        self.horizontalSlider_1_1240.setValue(trunc(self.B * self.w_2[3]))
        self.horizontalSlider_1_1250.setValue(trunc(self.B * self.w_2[4]))
        self.horizontalSlider_1_1260.setValue(trunc(self.B * self.w_2[5]))
        self.horizontalSlider_1_1200.setValue(trunc(self.B))
        self.horizontalSlider_1_1600.setValue(trunc(self.total))
    # period_2
    if period == 2:
        self.horizontalSlider_2_1110.setMaximum(trunc(self.A))
        self.horizontalSlider_2_1120.setMaximum(trunc(self.A))
        self.horizontalSlider_2_1130.setMaximum(trunc(self.A))
        self.horizontalSlider_2_1140.setMaximum(trunc(self.A))
        self.horizontalSlider_2_1150.setMaximum(trunc(self.A))
        self.horizontalSlider_2_1160.setMaximum(trunc(self.A))
        self.horizontalSlider_2_1170.setMaximum(trunc(self.A))
        self.horizontalSlider_2_1180.setMaximum(trunc(self.A))
        self.horizontalSlider_2_1190.setMaximum(trunc(self.A))
        self.horizontalSlider_2_1100.setMaximum(trunc(self.total))
        self.horizontalSlider_2_1110.setValue(trunc(self.A * self.w_1[0]))
        self.horizontalSlider_2_1120.setValue(trunc(self.A * self.w_1[1]))
        self.horizontalSlider_2_1130.setValue(trunc(self.A * self.w_1[2]))
        self.horizontalSlider_2_1140.setValue(trunc(self.A * self.w_1[3]))
        self.horizontalSlider_2_1150.setValue(trunc(self.A * 0.4))
        self.horizontalSlider_2_1160.setValue(trunc(self.A * self.w_1[4]))
        self.horizontalSlider_2_1170.setValue(trunc(self.A * 0.2))
        self.horizontalSlider_2_1180.setValue(trunc(self.A * self.w_1[5]))
        self.horizontalSlider_2_1190.setValue(trunc(self.A * self.w_1[6]))
        self.horizontalSlider_2_1100.setValue(trunc(self.A))
        self.horizontalSlider_2_1210.setMaximum(trunc(self.B))
        self.horizontalSlider_2_1220.setMaximum(trunc(self.B))
        self.horizontalSlider_2_1230.setMaximum(trunc(self.B))
        self.horizontalSlider_2_1240.setMaximum(trunc(self.B))
        self.horizontalSlider_2_1250.setMaximum(trunc(self.B))
        self.horizontalSlider_2_1260.setMaximum(trunc(self.B))
        self.horizontalSlider_2_1200.setMaximum(trunc(self.total))
        self.horizontalSlider_2_1600.setMaximum(trunc(self.total))
        self.horizontalSlider_2_1210.setValue(trunc(self.B * self.w_2[0]))
        self.horizontalSlider_2_1220.setValue(trunc(self.B * self.w_2[1]))
        self.horizontalSlider_2_1230.setValue(trunc(self.B * self.w_2[2]))
        self.horizontalSlider_2_1240.setValue(trunc(self.B * self.w_2[3]))
        self.horizontalSlider_2_1250.setValue(trunc(self.B * self.w_2[4]))
        self.horizontalSlider_2_1260.setValue(trunc(self.B * self.w_2[5]))
        self.horizontalSlider_2_1200.setValue(trunc(self.B))
        self.horizontalSlider_2_1600.setValue(trunc(self.total))
    # period_3
    if period == 3:
        self.horizontalSlider_3_1110.setMaximum(trunc(self.A))
        self.horizontalSlider_3_1120.setMaximum(trunc(self.A))
        self.horizontalSlider_3_1130.setMaximum(trunc(self.A))
        self.horizontalSlider_3_1140.setMaximum(trunc(self.A))
        self.horizontalSlider_3_1150.setMaximum(trunc(self.A))
        self.horizontalSlider_3_1160.setMaximum(trunc(self.A))
        self.horizontalSlider_3_1170.setMaximum(trunc(self.A))
        self.horizontalSlider_3_1180.setMaximum(trunc(self.A))
        self.horizontalSlider_3_1190.setMaximum(trunc(self.A))
        self.horizontalSlider_3_1100.setMaximum(trunc(self.total))
        self.horizontalSlider_3_1110.setValue(trunc(self.A * self.w_1[0]))
        self.horizontalSlider_3_1120.setValue(trunc(self.A * self.w_1[1]))
        self.horizontalSlider_3_1130.setValue(trunc(self.A * self.w_1[2]))
        self.horizontalSlider_3_1140.setValue(trunc(self.A * self.w_1[3]))
        self.horizontalSlider_3_1150.setValue(trunc(self.A * 0.4))
        self.horizontalSlider_3_1160.setValue(trunc(self.A * self.w_1[4]))
        self.horizontalSlider_3_1170.setValue(trunc(self.A * 0.2))
        self.horizontalSlider_3_1180.setValue(trunc(self.A * self.w_1[5]))
        self.horizontalSlider_3_1190.setValue(trunc(self.A * self.w_1[6]))
        self.horizontalSlider_3_1100.setValue(trunc(self.A))
        self.horizontalSlider_3_1210.setMaximum(trunc(self.B))
        self.horizontalSlider_3_1220.setMaximum(trunc(self.B))
        self.horizontalSlider_3_1230.setMaximum(trunc(self.B))
        self.horizontalSlider_3_1240.setMaximum(trunc(self.B))
        self.horizontalSlider_3_1250.setMaximum(trunc(self.B))
        self.horizontalSlider_3_1260.setMaximum(trunc(self.B))
        self.horizontalSlider_3_1200.setMaximum(trunc(self.total))
        self.horizontalSlider_3_1600.setMaximum(trunc(self.total))
        self.horizontalSlider_3_1210.setValue(trunc(self.B * self.w_2[0]))
        self.horizontalSlider_3_1220.setValue(trunc(self.B * self.w_2[1]))
        self.horizontalSlider_3_1230.setValue(trunc(self.B * self.w_2[2]))
        self.horizontalSlider_3_1240.setValue(trunc(self.B * self.w_2[3]))
        self.horizontalSlider_3_1250.setValue(trunc(self.B * self.w_2[4]))
        self.horizontalSlider_3_1260.setValue(trunc(self.B * self.w_2[5]))
        self.horizontalSlider_3_1200.setValue(trunc(self.B))
        self.horizontalSlider_3_1600.setValue(trunc(self.total))
    #пассив
    # period_0
    if period == 0:
        self.horizontalSlider_0_1310.setMaximum(trunc(self.C))
        self.horizontalSlider_0_1320.setMaximum(trunc(self.C))
        self.horizontalSlider_0_1340.setMaximum(trunc(self.C))
        self.horizontalSlider_0_1350.setMaximum(trunc(self.C))
        self.horizontalSlider_0_1360.setMaximum(trunc(self.C))
        self.horizontalSlider_0_1370.setMaximum(trunc(self.C))
        self.horizontalSlider_0_1300.setMaximum(trunc(self.total))
        self.horizontalSlider_0_1310.setValue(trunc(self.C * 0.05))
        self.horizontalSlider_0_1320.setValue(trunc(self.C * self.w_3[0]))
        self.horizontalSlider_0_1340.setValue(trunc(self.C * self.w_3[1]))
        self.horizontalSlider_0_1350.setValue(trunc(self.C * self.w_3[2]))
        self.horizontalSlider_0_1360.setValue(trunc(self.C * self.w_3[3]))
        self.horizontalSlider_0_1370.setValue(trunc(self.C * 0.9))
        self.horizontalSlider_0_1300.setValue(trunc(self.C))
        self.horizontalSlider_0_1410.setMaximum(trunc(self.D))
        self.horizontalSlider_0_1420.setMaximum(trunc(self.D))
        self.horizontalSlider_0_1430.setMaximum(trunc(self.D))
        self.horizontalSlider_0_1450.setMaximum(trunc(self.D))
        self.horizontalSlider_0_1400.setMaximum(trunc(self.total))
        self.horizontalSlider_0_1410.setValue(trunc(self.D * self.w_4[0]))
        self.horizontalSlider_0_1420.setValue(trunc(self.D * self.w_4[1]))
        self.horizontalSlider_0_1430.setValue(trunc(self.D * self.w_4[2]))
        self.horizontalSlider_0_1450.setValue(trunc(self.D * self.w_4[3]))
        self.horizontalSlider_0_1400.setValue(trunc(self.D))
        self.horizontalSlider_0_1510.setMaximum(trunc(self.E))
        self.horizontalSlider_0_1520.setMaximum(trunc(self.E))
        self.horizontalSlider_0_1530.setMaximum(trunc(self.E))
        self.horizontalSlider_0_1540.setMaximum(trunc(self.E))
        self.horizontalSlider_0_1550.setMaximum(trunc(self.E))
        self.horizontalSlider_0_1500.setMaximum(trunc(self.total))
        self.horizontalSlider_0_1700.setMaximum(trunc(self.total))
        self.horizontalSlider_0_1510.setValue(trunc(self.E * self.w_5[0]))
        self.horizontalSlider_0_1520.setValue(trunc(self.E * self.w_5[1]))
        self.horizontalSlider_0_1530.setValue(trunc(self.E * self.w_5[2]))
        self.horizontalSlider_0_1540.setValue(trunc(self.E * self.w_5[3]))
        self.horizontalSlider_0_1550.setValue(trunc(self.E * self.w_5[4]))
        self.horizontalSlider_0_1500.setValue(trunc(self.E))
        self.horizontalSlider_0_1700.setValue(trunc(self.total))
    # period_1
    if period == 1:
        self.horizontalSlider_1_1310.setMaximum(trunc(self.C))
        self.horizontalSlider_1_1320.setMaximum(trunc(self.C))
        self.horizontalSlider_1_1340.setMaximum(trunc(self.C))
        self.horizontalSlider_1_1350.setMaximum(trunc(self.C))
        self.horizontalSlider_1_1360.setMaximum(trunc(self.C))
        self.horizontalSlider_1_1370.setMaximum(trunc(self.C))
        self.horizontalSlider_1_1300.setMaximum(trunc(self.total))
        self.horizontalSlider_1_1310.setValue(trunc(self.C * 0.05))
        self.horizontalSlider_1_1320.setValue(trunc(self.C * self.w_3[0]))
        self.horizontalSlider_1_1340.setValue(trunc(self.C * self.w_3[1]))
        self.horizontalSlider_1_1350.setValue(trunc(self.C * self.w_3[2]))
        self.horizontalSlider_1_1360.setValue(trunc(self.C * self.w_3[3]))
        self.horizontalSlider_1_1370.setValue(trunc(self.C * 0.9))
        self.horizontalSlider_1_1300.setValue(trunc(self.C))
        self.horizontalSlider_1_1410.setMaximum(trunc(self.D))
        self.horizontalSlider_1_1420.setMaximum(trunc(self.D))
        self.horizontalSlider_1_1430.setMaximum(trunc(self.D))
        self.horizontalSlider_1_1450.setMaximum(trunc(self.D))
        self.horizontalSlider_1_1400.setMaximum(trunc(self.total))
        self.horizontalSlider_1_1410.setValue(trunc(self.D * self.w_4[0]))
        self.horizontalSlider_1_1420.setValue(trunc(self.D * self.w_4[1]))
        self.horizontalSlider_1_1430.setValue(trunc(self.D * self.w_4[2]))
        self.horizontalSlider_1_1450.setValue(trunc(self.D * self.w_4[3]))
        self.horizontalSlider_1_1400.setValue(trunc(self.D))
        self.horizontalSlider_1_1510.setMaximum(trunc(self.E))
        self.horizontalSlider_1_1520.setMaximum(trunc(self.E))
        self.horizontalSlider_1_1530.setMaximum(trunc(self.E))
        self.horizontalSlider_1_1540.setMaximum(trunc(self.E))
        self.horizontalSlider_1_1550.setMaximum(trunc(self.E))
        self.horizontalSlider_1_1500.setMaximum(trunc(self.total))
        self.horizontalSlider_1_1700.setMaximum(trunc(self.total))
        self.horizontalSlider_1_1510.setValue(trunc(self.E * self.w_5[0]))
        self.horizontalSlider_1_1520.setValue(trunc(self.E * self.w_5[1]))
        self.horizontalSlider_1_1530.setValue(trunc(self.E * self.w_5[2]))
        self.horizontalSlider_1_1540.setValue(trunc(self.E * self.w_5[3]))
        self.horizontalSlider_1_1550.setValue(trunc(self.E * self.w_5[4]))
        self.horizontalSlider_1_1500.setValue(trunc(self.E))
        self.horizontalSlider_1_1700.setValue(trunc(self.total))
    # period_2
    if period == 2:
        self.horizontalSlider_2_1310.setMaximum(trunc(self.C))
        self.horizontalSlider_2_1320.setMaximum(trunc(self.C))
        self.horizontalSlider_2_1340.setMaximum(trunc(self.C))
        self.horizontalSlider_2_1350.setMaximum(trunc(self.C))
        self.horizontalSlider_2_1360.setMaximum(trunc(self.C))
        self.horizontalSlider_2_1370.setMaximum(trunc(self.C))
        self.horizontalSlider_2_1300.setMaximum(trunc(self.total))
        self.horizontalSlider_2_1310.setValue(trunc(self.C * 0.05))
        self.horizontalSlider_2_1320.setValue(trunc(self.C * self.w_3[0]))
        self.horizontalSlider_2_1340.setValue(trunc(self.C * self.w_3[1]))
        self.horizontalSlider_2_1350.setValue(trunc(self.C * self.w_3[2]))
        self.horizontalSlider_2_1360.setValue(trunc(self.C * self.w_3[3]))
        self.horizontalSlider_2_1370.setValue(trunc(self.C * 0.9))
        self.horizontalSlider_2_1300.setValue(trunc(self.C))
        self.horizontalSlider_2_1410.setMaximum(trunc(self.D))
        self.horizontalSlider_2_1420.setMaximum(trunc(self.D))
        self.horizontalSlider_2_1430.setMaximum(trunc(self.D))
        self.horizontalSlider_2_1450.setMaximum(trunc(self.D))
        self.horizontalSlider_2_1400.setMaximum(trunc(self.total))
        self.horizontalSlider_2_1410.setValue(trunc(self.D * self.w_4[0]))
        self.horizontalSlider_2_1420.setValue(trunc(self.D * self.w_4[1]))
        self.horizontalSlider_2_1430.setValue(trunc(self.D * self.w_4[2]))
        self.horizontalSlider_2_1450.setValue(trunc(self.D * self.w_4[3]))
        self.horizontalSlider_2_1400.setValue(trunc(self.D))
        self.horizontalSlider_2_1510.setMaximum(trunc(self.E))
        self.horizontalSlider_2_1520.setMaximum(trunc(self.E))
        self.horizontalSlider_2_1530.setMaximum(trunc(self.E))
        self.horizontalSlider_2_1540.setMaximum(trunc(self.E))
        self.horizontalSlider_2_1550.setMaximum(trunc(self.E))
        self.horizontalSlider_2_1500.setMaximum(trunc(self.total))
        self.horizontalSlider_2_1700.setMaximum(trunc(self.total))
        self.horizontalSlider_2_1510.setValue(trunc(self.E * self.w_5[0]))
        self.horizontalSlider_2_1520.setValue(trunc(self.E * self.w_5[1]))
        self.horizontalSlider_2_1530.setValue(trunc(self.E * self.w_5[2]))
        self.horizontalSlider_2_1540.setValue(trunc(self.E * self.w_5[3]))
        self.horizontalSlider_2_1550.setValue(trunc(self.E * self.w_5[4]))
        self.horizontalSlider_2_1500.setValue(trunc(self.E))
        self.horizontalSlider_2_1700.setValue(trunc(self.total))
    # period_3
    if period == 3:
        self.horizontalSlider_3_1310.setMaximum(trunc(self.C))
        self.horizontalSlider_3_1320.setMaximum(trunc(self.C))
        self.horizontalSlider_3_1340.setMaximum(trunc(self.C))
        self.horizontalSlider_3_1350.setMaximum(trunc(self.C))
        self.horizontalSlider_3_1360.setMaximum(trunc(self.C))
        self.horizontalSlider_3_1370.setMaximum(trunc(self.C))
        self.horizontalSlider_3_1300.setMaximum(trunc(self.total))
        self.horizontalSlider_3_1310.setValue(trunc(self.C * 0.05))
        self.horizontalSlider_3_1320.setValue(trunc(self.C * self.w_3[0]))
        self.horizontalSlider_3_1340.setValue(trunc(self.C * self.w_3[1]))
        self.horizontalSlider_3_1350.setValue(trunc(self.C * self.w_3[2]))
        self.horizontalSlider_3_1360.setValue(trunc(self.C * self.w_3[3]))
        self.horizontalSlider_3_1370.setValue(trunc(self.C * 0.9))
        self.horizontalSlider_3_1300.setValue(trunc(self.C))
        self.horizontalSlider_3_1410.setMaximum(trunc(self.D))
        self.horizontalSlider_3_1420.setMaximum(trunc(self.D))
        self.horizontalSlider_3_1430.setMaximum(trunc(self.D))
        self.horizontalSlider_3_1450.setMaximum(trunc(self.D))
        self.horizontalSlider_3_1400.setMaximum(trunc(self.total))
        self.horizontalSlider_3_1410.setValue(trunc(self.D * self.w_4[0]))
        self.horizontalSlider_3_1420.setValue(trunc(self.D * self.w_4[1]))
        self.horizontalSlider_3_1430.setValue(trunc(self.D * self.w_4[2]))
        self.horizontalSlider_3_1450.setValue(trunc(self.D * self.w_4[3]))
        self.horizontalSlider_3_1400.setValue(trunc(self.D))
        self.horizontalSlider_3_1510.setMaximum(trunc(self.E))
        self.horizontalSlider_3_1520.setMaximum(trunc(self.E))
        self.horizontalSlider_3_1530.setMaximum(trunc(self.E))
        self.horizontalSlider_3_1540.setMaximum(trunc(self.E))
        self.horizontalSlider_3_1550.setMaximum(trunc(self.E))
        self.horizontalSlider_3_1500.setMaximum(trunc(self.total))
        self.horizontalSlider_3_1700.setMaximum(trunc(self.total))
        self.horizontalSlider_3_1510.setValue(trunc(self.E * self.w_5[0]))
        self.horizontalSlider_3_1520.setValue(trunc(self.E * self.w_5[1]))
        self.horizontalSlider_3_1530.setValue(trunc(self.E * self.w_5[2]))
        self.horizontalSlider_3_1540.setValue(trunc(self.E * self.w_5[3]))
        self.horizontalSlider_3_1550.setValue(trunc(self.E * self.w_5[4]))
        self.horizontalSlider_3_1500.setValue(trunc(self.E))
        self.horizontalSlider_3_1700.setValue(trunc(self.total))
    self.F = randint(0, 10_000_000)
    print('Выручка =', self.F)
    self.F_2120 = trunc(self.F * choice([0.5, 0.6, 0.7]))
    self.F_2100 = trunc(self.F - self.F_2120)
    self.F_2210 = trunc(self.F * choice([0.05, 0.06, 0.07]))
    self.F_2220 = trunc(self.F * choice([0.03, 0.04, 0.05]))
    self.F_2200 = trunc(self.F_2100 - self.F_2210 - self.F_2220)
    self.F_2310 = trunc(self.F * choice([0.001, 0.002, 0.003]))
    self.F_2320 = trunc(self.F * choice([0.002, 0.005, 0.01]))
    self.F_2330 = trunc(self.F * choice([0.004, 0.007, 0.01]))
    self.F_2340 = trunc(self.F * choice([0.01, 0.015, 0.02]))
    self.F_2350 = trunc(self.F * choice([0.047, 0.05, 0.03]))
    self.F_2300 = trunc(self.F_2200 + self.F_2320 - self.F_2330 + self.F_2310 + self.F_2340 - self.F_2350)
    self.F_2410 = trunc(self.F * choice([0.004, 0.006, 0.008]))
    self.F_2421 = trunc(self.F_2410 * choice([0.0001, 0.0005, 0.0007, 0.001, 0.005, 0.007]))
    self.F_2430 = trunc(self.F * choice([0.0001, 0.0005, 0.0007]))
    self.F_2450 = trunc(self.F * choice([0.0001, 0.0005, 0.0007]))
    self.F_2460 = trunc(self.F * choice([0.0001, 0.0005, 0.0007, 0.001, 0.005, 0.007]))
    self.F_2400 = trunc(self.F_2300 + self.F_2450 + self.F_2430 - self.F_2410 + self.F_2460)
    # ofr
    # period_0
    if period == 0:
        self.horizontalSlider_0_2110.setMaximum(self.F)
        self.horizontalSlider_0_2120.setMaximum(self.F)
        self.horizontalSlider_0_2100.setMaximum(self.F)
        self.horizontalSlider_0_2210.setMaximum(self.F_2100)
        self.horizontalSlider_0_2220.setMaximum(self.F_2100)
        self.horizontalSlider_0_2200.setMaximum(self.F_2100)
        self.horizontalSlider_0_2310.setMaximum(self.F_2100)
        self.horizontalSlider_0_2320.setMaximum(self.F_2100)
        self.horizontalSlider_0_2330.setMaximum(self.F_2100)
        self.horizontalSlider_0_2340.setMaximum(self.F_2100)
        self.horizontalSlider_0_2350.setMaximum(self.F_2100)
        self.horizontalSlider_0_2300.setMaximum(self.F_2100)
        self.horizontalSlider_0_2410.setMaximum(self.F_2100)
        self.horizontalSlider_0_2421.setMaximum(self.F_2100)
        self.horizontalSlider_0_2430.setMaximum(self.F_2100)
        self.horizontalSlider_0_2450.setMaximum(self.F_2100)
        self.horizontalSlider_0_2460.setMaximum(self.F_2100)
        self.horizontalSlider_0_2400.setMaximum(self.F_2100)
        self.horizontalSlider_0_2110.setValue(self.F)
        self.horizontalSlider_0_2120.setValue(self.F_2120)
        self.horizontalSlider_0_2100.setValue(self.F_2100)
        self.horizontalSlider_0_2210.setValue(self.F_2210)
        self.horizontalSlider_0_2220.setValue(self.F_2220)
        self.horizontalSlider_0_2200.setValue(self.F_2200)
        self.horizontalSlider_0_2310.setValue(self.F_2310)
        self.horizontalSlider_0_2320.setValue(self.F_2320)
        self.horizontalSlider_0_2330.setValue(self.F_2330)
        self.horizontalSlider_0_2340.setValue(self.F_2340)
        self.horizontalSlider_0_2350.setValue(self.F_2350)
        self.horizontalSlider_0_2300.setValue(self.F_2300)
        self.horizontalSlider_0_2410.setValue(self.F_2410)
        self.horizontalSlider_0_2421.setValue(self.F_2421)
        self.horizontalSlider_0_2430.setValue(self.F_2430)
        self.horizontalSlider_0_2450.setValue(self.F_2450)
        self.horizontalSlider_0_2460.setValue(self.F_2460)
        self.horizontalSlider_0_2400.setValue(self.F_2400)
    # period_1
    if period == 1:
        self.horizontalSlider_1_2110.setMaximum(self.F)
        self.horizontalSlider_1_2120.setMaximum(self.F)
        self.horizontalSlider_1_2100.setMaximum(self.F)
        self.horizontalSlider_1_2210.setMaximum(self.F_2100)
        self.horizontalSlider_1_2220.setMaximum(self.F_2100)
        self.horizontalSlider_1_2200.setMaximum(self.F_2100)
        self.horizontalSlider_1_2310.setMaximum(self.F_2100)
        self.horizontalSlider_1_2320.setMaximum(self.F_2100)
        self.horizontalSlider_1_2330.setMaximum(self.F_2100)
        self.horizontalSlider_1_2340.setMaximum(self.F_2100)
        self.horizontalSlider_1_2350.setMaximum(self.F_2100)
        self.horizontalSlider_1_2300.setMaximum(self.F_2100)
        self.horizontalSlider_1_2410.setMaximum(self.F_2100)
        self.horizontalSlider_1_2421.setMaximum(self.F_2100)
        self.horizontalSlider_1_2430.setMaximum(self.F_2100)
        self.horizontalSlider_1_2450.setMaximum(self.F_2100)
        self.horizontalSlider_1_2460.setMaximum(self.F_2100)
        self.horizontalSlider_1_2400.setMaximum(self.F_2100)
        self.horizontalSlider_1_2110.setValue(self.F)
        self.horizontalSlider_1_2120.setValue(self.F_2120)
        self.horizontalSlider_1_2100.setValue(self.F_2100)
        self.horizontalSlider_1_2210.setValue(self.F_2210)
        self.horizontalSlider_1_2220.setValue(self.F_2220)
        self.horizontalSlider_1_2200.setValue(self.F_2200)
        self.horizontalSlider_1_2310.setValue(self.F_2310)
        self.horizontalSlider_1_2320.setValue(self.F_2320)
        self.horizontalSlider_1_2330.setValue(self.F_2330)
        self.horizontalSlider_1_2340.setValue(self.F_2340)
        self.horizontalSlider_1_2350.setValue(self.F_2350)
        self.horizontalSlider_1_2300.setValue(self.F_2300)
        self.horizontalSlider_1_2410.setValue(self.F_2410)
        self.horizontalSlider_1_2421.setValue(self.F_2421)
        self.horizontalSlider_1_2430.setValue(self.F_2430)
        self.horizontalSlider_1_2450.setValue(self.F_2450)
        self.horizontalSlider_1_2460.setValue(self.F_2460)
        self.horizontalSlider_1_2400.setValue(self.F_2400)
    # period_2
    if period == 2:
        self.horizontalSlider_2_2110.setMaximum(self.F)
        self.horizontalSlider_2_2120.setMaximum(self.F)
        self.horizontalSlider_2_2100.setMaximum(self.F)
        self.horizontalSlider_2_2210.setMaximum(self.F_2100)
        self.horizontalSlider_2_2220.setMaximum(self.F_2100)
        self.horizontalSlider_2_2200.setMaximum(self.F_2100)
        self.horizontalSlider_2_2310.setMaximum(self.F_2100)
        self.horizontalSlider_2_2320.setMaximum(self.F_2100)
        self.horizontalSlider_2_2330.setMaximum(self.F_2100)
        self.horizontalSlider_2_2340.setMaximum(self.F_2100)
        self.horizontalSlider_2_2350.setMaximum(self.F_2100)
        self.horizontalSlider_2_2300.setMaximum(self.F_2100)
        self.horizontalSlider_2_2410.setMaximum(self.F_2100)
        self.horizontalSlider_2_2421.setMaximum(self.F_2100)
        self.horizontalSlider_2_2430.setMaximum(self.F_2100)
        self.horizontalSlider_2_2450.setMaximum(self.F_2100)
        self.horizontalSlider_2_2460.setMaximum(self.F_2100)
        self.horizontalSlider_2_2400.setMaximum(self.F_2100)
        self.horizontalSlider_2_2110.setValue(self.F)
        self.horizontalSlider_2_2120.setValue(self.F_2120)
        self.horizontalSlider_2_2100.setValue(self.F_2100)
        self.horizontalSlider_2_2210.setValue(self.F_2210)
        self.horizontalSlider_2_2220.setValue(self.F_2220)
        self.horizontalSlider_2_2200.setValue(self.F_2200)
        self.horizontalSlider_2_2310.setValue(self.F_2310)
        self.horizontalSlider_2_2320.setValue(self.F_2320)
        self.horizontalSlider_2_2330.setValue(self.F_2330)
        self.horizontalSlider_2_2340.setValue(self.F_2340)
        self.horizontalSlider_2_2350.setValue(self.F_2350)
        self.horizontalSlider_2_2300.setValue(self.F_2300)
        self.horizontalSlider_2_2410.setValue(self.F_2410)
        self.horizontalSlider_2_2421.setValue(self.F_2421)
        self.horizontalSlider_2_2430.setValue(self.F_2430)
        self.horizontalSlider_2_2450.setValue(self.F_2450)
        self.horizontalSlider_2_2460.setValue(self.F_2460)
        self.horizontalSlider_2_2400.setValue(self.F_2400)
    # period_3
    if period == 3:
        self.horizontalSlider_3_2110.setMaximum(self.F)
        self.horizontalSlider_3_2120.setMaximum(self.F)
        self.horizontalSlider_3_2100.setMaximum(self.F)
        self.horizontalSlider_3_2210.setMaximum(self.F_2100)
        self.horizontalSlider_3_2220.setMaximum(self.F_2100)
        self.horizontalSlider_3_2200.setMaximum(self.F_2100)
        self.horizontalSlider_3_2310.setMaximum(self.F_2100)
        self.horizontalSlider_3_2320.setMaximum(self.F_2100)
        self.horizontalSlider_3_2330.setMaximum(self.F_2100)
        self.horizontalSlider_3_2340.setMaximum(self.F_2100)
        self.horizontalSlider_3_2350.setMaximum(self.F_2100)
        self.horizontalSlider_3_2300.setMaximum(self.F_2100)
        self.horizontalSlider_3_2410.setMaximum(self.F_2100)
        self.horizontalSlider_3_2421.setMaximum(self.F_2100)
        self.horizontalSlider_3_2430.setMaximum(self.F_2100)
        self.horizontalSlider_3_2450.setMaximum(self.F_2100)
        self.horizontalSlider_3_2460.setMaximum(self.F_2100)
        self.horizontalSlider_3_2400.setMaximum(self.F_2100)
        self.horizontalSlider_3_2110.setValue(self.F)
        self.horizontalSlider_3_2120.setValue(self.F_2120)
        self.horizontalSlider_3_2100.setValue(self.F_2100)
        self.horizontalSlider_3_2210.setValue(self.F_2210)
        self.horizontalSlider_3_2220.setValue(self.F_2220)
        self.horizontalSlider_3_2200.setValue(self.F_2200)
        self.horizontalSlider_3_2310.setValue(self.F_2310)
        self.horizontalSlider_3_2320.setValue(self.F_2320)
        self.horizontalSlider_3_2330.setValue(self.F_2330)
        self.horizontalSlider_3_2340.setValue(self.F_2340)
        self.horizontalSlider_3_2350.setValue(self.F_2350)
        self.horizontalSlider_3_2300.setValue(self.F_2300)
        self.horizontalSlider_3_2410.setValue(self.F_2410)
        self.horizontalSlider_3_2421.setValue(self.F_2421)
        self.horizontalSlider_3_2430.setValue(self.F_2430)
        self.horizontalSlider_3_2450.setValue(self.F_2450)
        self.horizontalSlider_3_2460.setValue(self.F_2460)
        self.horizontalSlider_3_2400.setValue(self.F_2400)
def clear_button_active(self):
    # period_0
    self.horizontalSlider_0_1110.setValue(0)
    self.horizontalSlider_0_1120.setValue(0)
    self.horizontalSlider_0_1130.setValue(0)
    self.horizontalSlider_0_1140.setValue(0)
    self.horizontalSlider_0_1150.setValue(0)
    self.horizontalSlider_0_1160.setValue(0)
    self.horizontalSlider_0_1170.setValue(0)
    self.horizontalSlider_0_1180.setValue(0)
    self.horizontalSlider_0_1190.setValue(0)
    self.horizontalSlider_0_1100.setValue(0)
    self.horizontalSlider_0_1210.setValue(0)
    self.horizontalSlider_0_1220.setValue(0)
    self.horizontalSlider_0_1230.setValue(0)
    self.horizontalSlider_0_1240.setValue(0)
    self.horizontalSlider_0_1250.setValue(0)
    self.horizontalSlider_0_1260.setValue(0)
    self.horizontalSlider_0_1200.setValue(0)
    self.horizontalSlider_0_1600.setValue(0)
    # period_1
    self.horizontalSlider_1_1110.setValue(0)
    self.horizontalSlider_1_1120.setValue(0)
    self.horizontalSlider_1_1130.setValue(0)
    self.horizontalSlider_1_1140.setValue(0)
    self.horizontalSlider_1_1150.setValue(0)
    self.horizontalSlider_1_1160.setValue(0)
    self.horizontalSlider_1_1170.setValue(0)
    self.horizontalSlider_1_1180.setValue(0)
    self.horizontalSlider_1_1190.setValue(0)
    self.horizontalSlider_1_1100.setValue(0)
    self.horizontalSlider_1_1210.setValue(0)
    self.horizontalSlider_1_1220.setValue(0)
    self.horizontalSlider_1_1230.setValue(0)
    self.horizontalSlider_1_1240.setValue(0)
    self.horizontalSlider_1_1250.setValue(0)
    self.horizontalSlider_1_1260.setValue(0)
    self.horizontalSlider_1_1200.setValue(0)
    self.horizontalSlider_1_1600.setValue(0)
    # period_2
    self.horizontalSlider_2_1110.setValue(0)
    self.horizontalSlider_2_1120.setValue(0)
    self.horizontalSlider_2_1130.setValue(0)
    self.horizontalSlider_2_1140.setValue(0)
    self.horizontalSlider_2_1150.setValue(0)
    self.horizontalSlider_2_1160.setValue(0)
    self.horizontalSlider_2_1170.setValue(0)
    self.horizontalSlider_2_1180.setValue(0)
    self.horizontalSlider_2_1190.setValue(0)
    self.horizontalSlider_2_1100.setValue(0)
    self.horizontalSlider_2_1210.setValue(0)
    self.horizontalSlider_2_1220.setValue(0)
    self.horizontalSlider_2_1230.setValue(0)
    self.horizontalSlider_2_1240.setValue(0)
    self.horizontalSlider_2_1250.setValue(0)
    self.horizontalSlider_2_1260.setValue(0)
    self.horizontalSlider_2_1200.setValue(0)
    self.horizontalSlider_2_1600.setValue(0)
    # period_3
    self.horizontalSlider_3_1110.setValue(0)
    self.horizontalSlider_3_1120.setValue(0)
    self.horizontalSlider_3_1130.setValue(0)
    self.horizontalSlider_3_1140.setValue(0)
    self.horizontalSlider_3_1150.setValue(0)
    self.horizontalSlider_3_1160.setValue(0)
    self.horizontalSlider_3_1170.setValue(0)
    self.horizontalSlider_3_1180.setValue(0)
    self.horizontalSlider_3_1190.setValue(0)
    self.horizontalSlider_3_1100.setValue(0)
    self.horizontalSlider_3_1210.setValue(0)
    self.horizontalSlider_3_1220.setValue(0)
    self.horizontalSlider_3_1230.setValue(0)
    self.horizontalSlider_3_1240.setValue(0)
    self.horizontalSlider_3_1250.setValue(0)
    self.horizontalSlider_3_1260.setValue(0)
    self.horizontalSlider_3_1200.setValue(0)
    self.horizontalSlider_3_1600.setValue(0)
def clear_button_passive(self):
    # period_0
    self.horizontalSlider_0_1310.setValue(0)
    self.horizontalSlider_0_1320.setValue(0)
    self.horizontalSlider_0_1340.setValue(0)
    self.horizontalSlider_0_1350.setValue(0)
    self.horizontalSlider_0_1360.setValue(0)
    self.horizontalSlider_0_1370.setValue(0)
    self.horizontalSlider_0_1300.setValue(0)
    self.horizontalSlider_0_1410.setValue(0)
    self.horizontalSlider_0_1420.setValue(0)
    self.horizontalSlider_0_1430.setValue(0)
    self.horizontalSlider_0_1450.setValue(0)
    self.horizontalSlider_0_1400.setValue(0)
    self.horizontalSlider_0_1510.setValue(0)
    self.horizontalSlider_0_1520.setValue(0)
    self.horizontalSlider_0_1530.setValue(0)
    self.horizontalSlider_0_1540.setValue(0)
    self.horizontalSlider_0_1550.setValue(0)
    self.horizontalSlider_0_1500.setValue(0)
    self.horizontalSlider_0_1700.setValue(0)
    # period_1
    self.horizontalSlider_1_1310.setValue(0)
    self.horizontalSlider_1_1320.setValue(0)
    self.horizontalSlider_1_1340.setValue(0)
    self.horizontalSlider_1_1350.setValue(0)
    self.horizontalSlider_1_1360.setValue(0)
    self.horizontalSlider_1_1370.setValue(0)
    self.horizontalSlider_1_1300.setValue(0)
    self.horizontalSlider_1_1410.setValue(0)
    self.horizontalSlider_1_1420.setValue(0)
    self.horizontalSlider_1_1430.setValue(0)
    self.horizontalSlider_1_1450.setValue(0)
    self.horizontalSlider_1_1400.setValue(0)
    self.horizontalSlider_1_1510.setValue(0)
    self.horizontalSlider_1_1520.setValue(0)
    self.horizontalSlider_1_1530.setValue(0)
    self.horizontalSlider_1_1540.setValue(0)
    self.horizontalSlider_1_1550.setValue(0)
    self.horizontalSlider_1_1500.setValue(0)
    self.horizontalSlider_1_1700.setValue(0)
    # period_2
    self.horizontalSlider_2_1310.setValue(0)
    self.horizontalSlider_2_1320.setValue(0)
    self.horizontalSlider_2_1340.setValue(0)
    self.horizontalSlider_2_1350.setValue(0)
    self.horizontalSlider_2_1360.setValue(0)
    self.horizontalSlider_2_1370.setValue(0)
    self.horizontalSlider_2_1300.setValue(0)
    self.horizontalSlider_2_1410.setValue(0)
    self.horizontalSlider_2_1420.setValue(0)
    self.horizontalSlider_2_1430.setValue(0)
    self.horizontalSlider_2_1450.setValue(0)
    self.horizontalSlider_2_1400.setValue(0)
    self.horizontalSlider_2_1510.setValue(0)
    self.horizontalSlider_2_1520.setValue(0)
    self.horizontalSlider_2_1530.setValue(0)
    self.horizontalSlider_2_1540.setValue(0)
    self.horizontalSlider_2_1550.setValue(0)
    self.horizontalSlider_2_1500.setValue(0)
    self.horizontalSlider_2_1700.setValue(0)
    # period_3
    self.horizontalSlider_3_1310.setValue(0)
    self.horizontalSlider_3_1320.setValue(0)
    self.horizontalSlider_3_1340.setValue(0)
    self.horizontalSlider_3_1350.setValue(0)
    self.horizontalSlider_3_1360.setValue(0)
    self.horizontalSlider_3_1370.setValue(0)
    self.horizontalSlider_3_1300.setValue(0)
    self.horizontalSlider_3_1410.setValue(0)
    self.horizontalSlider_3_1420.setValue(0)
    self.horizontalSlider_3_1430.setValue(0)
    self.horizontalSlider_3_1450.setValue(0)
    self.horizontalSlider_3_1400.setValue(0)
    self.horizontalSlider_3_1510.setValue(0)
    self.horizontalSlider_3_1520.setValue(0)
    self.horizontalSlider_3_1530.setValue(0)
    self.horizontalSlider_3_1540.setValue(0)
    self.horizontalSlider_3_1550.setValue(0)
    self.horizontalSlider_3_1500.setValue(0)
    self.horizontalSlider_3_1700.setValue(0)
def clear_button_ofr(self):
    #0
    self.horizontalSlider_0_2110.setValue(0)
    self.horizontalSlider_0_2120.setValue(0)
    self.horizontalSlider_0_2100.setValue(0)
    self.horizontalSlider_0_2210.setValue(0)
    self.horizontalSlider_0_2220.setValue(0)
    self.horizontalSlider_0_2200.setValue(0)
    self.horizontalSlider_0_2310.setValue(0)
    self.horizontalSlider_0_2320.setValue(0)
    self.horizontalSlider_0_2330.setValue(0)
    self.horizontalSlider_0_2340.setValue(0)
    self.horizontalSlider_0_2350.setValue(0)
    self.horizontalSlider_0_2300.setValue(0)
    self.horizontalSlider_0_2410.setValue(0)
    self.horizontalSlider_0_2421.setValue(0)
    self.horizontalSlider_0_2430.setValue(0)
    self.horizontalSlider_0_2450.setValue(0)
    self.horizontalSlider_0_2460.setValue(0)
    self.horizontalSlider_0_2400.setValue(0)
    # 1
    self.horizontalSlider_1_2110.setValue(0)
    self.horizontalSlider_1_2120.setValue(0)
    self.horizontalSlider_1_2100.setValue(0)
    self.horizontalSlider_1_2210.setValue(0)
    self.horizontalSlider_1_2220.setValue(0)
    self.horizontalSlider_1_2200.setValue(0)
    self.horizontalSlider_1_2310.setValue(0)
    self.horizontalSlider_1_2320.setValue(0)
    self.horizontalSlider_1_2330.setValue(0)
    self.horizontalSlider_1_2340.setValue(0)
    self.horizontalSlider_1_2350.setValue(0)
    self.horizontalSlider_1_2300.setValue(0)
    self.horizontalSlider_1_2410.setValue(0)
    self.horizontalSlider_1_2421.setValue(0)
    self.horizontalSlider_1_2430.setValue(0)
    self.horizontalSlider_1_2450.setValue(0)
    self.horizontalSlider_1_2460.setValue(0)
    self.horizontalSlider_1_2400.setValue(0)
    # 2
    self.horizontalSlider_2_2110.setValue(0)
    self.horizontalSlider_2_2120.setValue(0)
    self.horizontalSlider_2_2100.setValue(0)
    self.horizontalSlider_2_2210.setValue(0)
    self.horizontalSlider_2_2220.setValue(0)
    self.horizontalSlider_2_2200.setValue(0)
    self.horizontalSlider_2_2310.setValue(0)
    self.horizontalSlider_2_2320.setValue(0)
    self.horizontalSlider_2_2330.setValue(0)
    self.horizontalSlider_2_2340.setValue(0)
    self.horizontalSlider_2_2350.setValue(0)
    self.horizontalSlider_2_2300.setValue(0)
    self.horizontalSlider_2_2410.setValue(0)
    self.horizontalSlider_2_2421.setValue(0)
    self.horizontalSlider_2_2430.setValue(0)
    self.horizontalSlider_2_2450.setValue(0)
    self.horizontalSlider_2_2460.setValue(0)
    self.horizontalSlider_2_2400.setValue(0)
    # 3
    self.horizontalSlider_3_2110.setValue(0)
    self.horizontalSlider_3_2120.setValue(0)
    self.horizontalSlider_3_2100.setValue(0)
    self.horizontalSlider_3_2210.setValue(0)
    self.horizontalSlider_3_2220.setValue(0)
    self.horizontalSlider_3_2200.setValue(0)
    self.horizontalSlider_3_2310.setValue(0)
    self.horizontalSlider_3_2320.setValue(0)
    self.horizontalSlider_3_2330.setValue(0)
    self.horizontalSlider_3_2340.setValue(0)
    self.horizontalSlider_3_2350.setValue(0)
    self.horizontalSlider_3_2300.setValue(0)
    self.horizontalSlider_3_2410.setValue(0)
    self.horizontalSlider_3_2421.setValue(0)
    self.horizontalSlider_3_2430.setValue(0)
    self.horizontalSlider_3_2450.setValue(0)
    self.horizontalSlider_3_2460.setValue(0)
    self.horizontalSlider_3_2400.setValue(0)
def click_checkbox(self, state):
    if state == QtCore.Qt.Checked:
        self.frame.setHidden(True)
        self.frame_2.setHidden(True)
        self.frame_3.setHidden(True)
        self.frame_7.setHidden(True)
        self.frame_4.setHidden(True)
        self.frame_5.setHidden(True)
        self.frame_6.setHidden(True)
        self.frame_12.setHidden(True)
        #ofr
        self.frame_8.setHidden(True)
        self.frame_9.setHidden(True)
        self.frame_10.setHidden(True)
        self.frame_11.setHidden(True)
        #period_0
        self.horizontalSlider_0_1110.setDisabled(True)
        self.horizontalSlider_0_1120.setDisabled(True)
        self.horizontalSlider_0_1130.setDisabled(True)
        self.horizontalSlider_0_1140.setDisabled(True)
        self.horizontalSlider_0_1150.setDisabled(True)
        self.horizontalSlider_0_1160.setDisabled(True)
        self.horizontalSlider_0_1170.setDisabled(True)
        self.horizontalSlider_0_1180.setDisabled(True)
        self.horizontalSlider_0_1190.setDisabled(True)
        self.horizontalSlider_0_1100.setDisabled(True)
        self.horizontalSlider_0_1210.setDisabled(True)
        self.horizontalSlider_0_1220.setDisabled(True)
        self.horizontalSlider_0_1230.setDisabled(True)
        self.horizontalSlider_0_1240.setDisabled(True)
        self.horizontalSlider_0_1250.setDisabled(True)
        self.horizontalSlider_0_1260.setDisabled(True)
        self.horizontalSlider_0_1600.setDisabled(True)
        self.horizontalSlider_0_1200.setDisabled(True)
        self.horizontalSlider_0_1310.setDisabled(True)
        self.horizontalSlider_0_1320.setDisabled(True)
        self.horizontalSlider_0_1340.setDisabled(True)
        self.horizontalSlider_0_1350.setDisabled(True)
        self.horizontalSlider_0_1360.setDisabled(True)
        self.horizontalSlider_0_1370.setDisabled(True)
        self.horizontalSlider_0_1300.setDisabled(True)
        self.horizontalSlider_0_1410.setDisabled(True)
        self.horizontalSlider_0_1420.setDisabled(True)
        self.horizontalSlider_0_1430.setDisabled(True)
        self.horizontalSlider_0_1450.setDisabled(True)
        self.horizontalSlider_0_1400.setDisabled(True)
        self.horizontalSlider_0_1510.setDisabled(True)
        self.horizontalSlider_0_1520.setDisabled(True)
        self.horizontalSlider_0_1530.setDisabled(True)
        self.horizontalSlider_0_1540.setDisabled(True)
        self.horizontalSlider_0_1550.setDisabled(True)
        self.horizontalSlider_0_1500.setDisabled(True)
        self.horizontalSlider_0_1700.setDisabled(True)
        self.horizontalSlider_0_2110.setDisabled(True)
        self.horizontalSlider_0_2120.setDisabled(True)
        self.horizontalSlider_0_2100.setDisabled(True)
        self.horizontalSlider_0_2210.setDisabled(True)
        self.horizontalSlider_0_2220.setDisabled(True)
        self.horizontalSlider_0_2200.setDisabled(True)
        self.horizontalSlider_0_2310.setDisabled(True)
        self.horizontalSlider_0_2320.setDisabled(True)
        self.horizontalSlider_0_2330.setDisabled(True)
        self.horizontalSlider_0_2340.setDisabled(True)
        self.horizontalSlider_0_2350.setDisabled(True)
        self.horizontalSlider_0_2300.setDisabled(True)
        self.horizontalSlider_0_2410.setDisabled(True)
        self.horizontalSlider_0_2421.setDisabled(True)
        self.horizontalSlider_0_2430.setDisabled(True)
        self.horizontalSlider_0_2450.setDisabled(True)
        self.horizontalSlider_0_2460.setDisabled(True)
        self.horizontalSlider_0_2400.setDisabled(True)
        #period_1
        self.horizontalSlider_1_1110.setDisabled(True)
        self.horizontalSlider_1_1120.setDisabled(True)
        self.horizontalSlider_1_1130.setDisabled(True)
        self.horizontalSlider_1_1140.setDisabled(True)
        self.horizontalSlider_1_1150.setDisabled(True)
        self.horizontalSlider_1_1160.setDisabled(True)
        self.horizontalSlider_1_1170.setDisabled(True)
        self.horizontalSlider_1_1180.setDisabled(True)
        self.horizontalSlider_1_1190.setDisabled(True)
        self.horizontalSlider_1_1100.setDisabled(True)
        self.horizontalSlider_1_1210.setDisabled(True)
        self.horizontalSlider_1_1220.setDisabled(True)
        self.horizontalSlider_1_1230.setDisabled(True)
        self.horizontalSlider_1_1240.setDisabled(True)
        self.horizontalSlider_1_1250.setDisabled(True)
        self.horizontalSlider_1_1260.setDisabled(True)
        self.horizontalSlider_1_1600.setDisabled(True)
        self.horizontalSlider_1_1200.setDisabled(True)
        self.horizontalSlider_1_1310.setDisabled(True)
        self.horizontalSlider_1_1320.setDisabled(True)
        self.horizontalSlider_1_1340.setDisabled(True)
        self.horizontalSlider_1_1350.setDisabled(True)
        self.horizontalSlider_1_1360.setDisabled(True)
        self.horizontalSlider_1_1370.setDisabled(True)
        self.horizontalSlider_1_1300.setDisabled(True)
        self.horizontalSlider_1_1410.setDisabled(True)
        self.horizontalSlider_1_1420.setDisabled(True)
        self.horizontalSlider_1_1430.setDisabled(True)
        self.horizontalSlider_1_1450.setDisabled(True)
        self.horizontalSlider_1_1400.setDisabled(True)
        self.horizontalSlider_1_1510.setDisabled(True)
        self.horizontalSlider_1_1520.setDisabled(True)
        self.horizontalSlider_1_1530.setDisabled(True)
        self.horizontalSlider_1_1540.setDisabled(True)
        self.horizontalSlider_1_1550.setDisabled(True)
        self.horizontalSlider_1_1500.setDisabled(True)
        self.horizontalSlider_1_1700.setDisabled(True)
        self.horizontalSlider_1_2110.setDisabled(True)
        self.horizontalSlider_1_2120.setDisabled(True)
        self.horizontalSlider_1_2100.setDisabled(True)
        self.horizontalSlider_1_2210.setDisabled(True)
        self.horizontalSlider_1_2220.setDisabled(True)
        self.horizontalSlider_1_2200.setDisabled(True)
        self.horizontalSlider_1_2310.setDisabled(True)
        self.horizontalSlider_1_2320.setDisabled(True)
        self.horizontalSlider_1_2330.setDisabled(True)
        self.horizontalSlider_1_2340.setDisabled(True)
        self.horizontalSlider_1_2350.setDisabled(True)
        self.horizontalSlider_1_2300.setDisabled(True)
        self.horizontalSlider_1_2410.setDisabled(True)
        self.horizontalSlider_1_2421.setDisabled(True)
        self.horizontalSlider_1_2430.setDisabled(True)
        self.horizontalSlider_1_2450.setDisabled(True)
        self.horizontalSlider_1_2460.setDisabled(True)
        self.horizontalSlider_1_2400.setDisabled(True)
        #period_2
        self.horizontalSlider_2_1110.setDisabled(True)
        self.horizontalSlider_2_1120.setDisabled(True)
        self.horizontalSlider_2_1130.setDisabled(True)
        self.horizontalSlider_2_1140.setDisabled(True)
        self.horizontalSlider_2_1150.setDisabled(True)
        self.horizontalSlider_2_1160.setDisabled(True)
        self.horizontalSlider_2_1170.setDisabled(True)
        self.horizontalSlider_2_1180.setDisabled(True)
        self.horizontalSlider_2_1190.setDisabled(True)
        self.horizontalSlider_2_1100.setDisabled(True)
        self.horizontalSlider_2_1210.setDisabled(True)
        self.horizontalSlider_2_1220.setDisabled(True)
        self.horizontalSlider_2_1230.setDisabled(True)
        self.horizontalSlider_2_1240.setDisabled(True)
        self.horizontalSlider_2_1250.setDisabled(True)
        self.horizontalSlider_2_1260.setDisabled(True)
        self.horizontalSlider_2_1600.setDisabled(True)
        self.horizontalSlider_2_1200.setDisabled(True)
        self.horizontalSlider_2_1310.setDisabled(True)
        self.horizontalSlider_2_1320.setDisabled(True)
        self.horizontalSlider_2_1340.setDisabled(True)
        self.horizontalSlider_2_1350.setDisabled(True)
        self.horizontalSlider_2_1360.setDisabled(True)
        self.horizontalSlider_2_1370.setDisabled(True)
        self.horizontalSlider_2_1300.setDisabled(True)
        self.horizontalSlider_2_1410.setDisabled(True)
        self.horizontalSlider_2_1420.setDisabled(True)
        self.horizontalSlider_2_1430.setDisabled(True)
        self.horizontalSlider_2_1450.setDisabled(True)
        self.horizontalSlider_2_1400.setDisabled(True)
        self.horizontalSlider_2_1510.setDisabled(True)
        self.horizontalSlider_2_1520.setDisabled(True)
        self.horizontalSlider_2_1530.setDisabled(True)
        self.horizontalSlider_2_1540.setDisabled(True)
        self.horizontalSlider_2_1550.setDisabled(True)
        self.horizontalSlider_2_1500.setDisabled(True)
        self.horizontalSlider_2_1700.setDisabled(True)
        self.horizontalSlider_2_2110.setDisabled(True)
        self.horizontalSlider_2_2120.setDisabled(True)
        self.horizontalSlider_2_2100.setDisabled(True)
        self.horizontalSlider_2_2210.setDisabled(True)
        self.horizontalSlider_2_2220.setDisabled(True)
        self.horizontalSlider_2_2200.setDisabled(True)
        self.horizontalSlider_2_2310.setDisabled(True)
        self.horizontalSlider_2_2320.setDisabled(True)
        self.horizontalSlider_2_2330.setDisabled(True)
        self.horizontalSlider_2_2340.setDisabled(True)
        self.horizontalSlider_2_2350.setDisabled(True)
        self.horizontalSlider_2_2300.setDisabled(True)
        self.horizontalSlider_2_2410.setDisabled(True)
        self.horizontalSlider_2_2421.setDisabled(True)
        self.horizontalSlider_2_2430.setDisabled(True)
        self.horizontalSlider_2_2450.setDisabled(True)
        self.horizontalSlider_2_2460.setDisabled(True)
        self.horizontalSlider_2_2400.setDisabled(True)
        #period_3
        self.horizontalSlider_3_1110.setDisabled(True)
        self.horizontalSlider_3_1120.setDisabled(True)
        self.horizontalSlider_3_1130.setDisabled(True)
        self.horizontalSlider_3_1140.setDisabled(True)
        self.horizontalSlider_3_1150.setDisabled(True)
        self.horizontalSlider_3_1160.setDisabled(True)
        self.horizontalSlider_3_1170.setDisabled(True)
        self.horizontalSlider_3_1180.setDisabled(True)
        self.horizontalSlider_3_1190.setDisabled(True)
        self.horizontalSlider_3_1100.setDisabled(True)
        self.horizontalSlider_3_1210.setDisabled(True)
        self.horizontalSlider_3_1220.setDisabled(True)
        self.horizontalSlider_3_1230.setDisabled(True)
        self.horizontalSlider_3_1240.setDisabled(True)
        self.horizontalSlider_3_1250.setDisabled(True)
        self.horizontalSlider_3_1260.setDisabled(True)
        self.horizontalSlider_3_1600.setDisabled(True)
        self.horizontalSlider_3_1200.setDisabled(True)
        self.horizontalSlider_3_1310.setDisabled(True)
        self.horizontalSlider_3_1320.setDisabled(True)
        self.horizontalSlider_3_1340.setDisabled(True)
        self.horizontalSlider_3_1350.setDisabled(True)
        self.horizontalSlider_3_1360.setDisabled(True)
        self.horizontalSlider_3_1370.setDisabled(True)
        self.horizontalSlider_3_1300.setDisabled(True)
        self.horizontalSlider_3_1410.setDisabled(True)
        self.horizontalSlider_3_1420.setDisabled(True)
        self.horizontalSlider_3_1430.setDisabled(True)
        self.horizontalSlider_3_1450.setDisabled(True)
        self.horizontalSlider_3_1400.setDisabled(True)
        self.horizontalSlider_3_1510.setDisabled(True)
        self.horizontalSlider_3_1520.setDisabled(True)
        self.horizontalSlider_3_1530.setDisabled(True)
        self.horizontalSlider_3_1540.setDisabled(True)
        self.horizontalSlider_3_1550.setDisabled(True)
        self.horizontalSlider_3_1500.setDisabled(True)
        self.horizontalSlider_3_1700.setDisabled(True)
        self.horizontalSlider_3_2110.setDisabled(True)
        self.horizontalSlider_3_2120.setDisabled(True)
        self.horizontalSlider_3_2100.setDisabled(True)
        self.horizontalSlider_3_2210.setDisabled(True)
        self.horizontalSlider_3_2220.setDisabled(True)
        self.horizontalSlider_3_2200.setDisabled(True)
        self.horizontalSlider_3_2310.setDisabled(True)
        self.horizontalSlider_3_2320.setDisabled(True)
        self.horizontalSlider_3_2330.setDisabled(True)
        self.horizontalSlider_3_2340.setDisabled(True)
        self.horizontalSlider_3_2350.setDisabled(True)
        self.horizontalSlider_3_2300.setDisabled(True)
        self.horizontalSlider_3_2410.setDisabled(True)
        self.horizontalSlider_3_2421.setDisabled(True)
        self.horizontalSlider_3_2430.setDisabled(True)
        self.horizontalSlider_3_2450.setDisabled(True)
        self.horizontalSlider_3_2460.setDisabled(True)
        self.horizontalSlider_3_2400.setDisabled(True)
    else:
        self.frame.setHidden(False)
        self.frame_2.setHidden(False)
        self.frame_3.setHidden(False)
        self.frame_7.setHidden(False)
        self.frame_4.setHidden(False)
        self.frame_5.setHidden(False)
        self.frame_6.setHidden(False)
        self.frame_12.setHidden(False)
        #ofr
        self.frame_8.setHidden(False)
        self.frame_9.setHidden(False)
        self.frame_10.setHidden(False)
        self.frame_11.setHidden(False)
        #period_0
        self.horizontalSlider_0_1110.setDisabled(False)
        self.horizontalSlider_0_1120.setDisabled(False)
        self.horizontalSlider_0_1130.setDisabled(False)
        self.horizontalSlider_0_1140.setDisabled(False)
        self.horizontalSlider_0_1150.setDisabled(False)
        self.horizontalSlider_0_1160.setDisabled(False)
        self.horizontalSlider_0_1170.setDisabled(False)
        self.horizontalSlider_0_1180.setDisabled(False)
        self.horizontalSlider_0_1190.setDisabled(False)
        self.horizontalSlider_0_1100.setDisabled(False)
        self.horizontalSlider_0_1210.setDisabled(False)
        self.horizontalSlider_0_1220.setDisabled(False)
        self.horizontalSlider_0_1230.setDisabled(False)
        self.horizontalSlider_0_1240.setDisabled(False)
        self.horizontalSlider_0_1250.setDisabled(False)
        self.horizontalSlider_0_1260.setDisabled(False)
        self.horizontalSlider_0_1600.setDisabled(False)
        self.horizontalSlider_0_1200.setDisabled(False)
        self.horizontalSlider_0_1310.setDisabled(False)
        self.horizontalSlider_0_1320.setDisabled(False)
        self.horizontalSlider_0_1340.setDisabled(False)
        self.horizontalSlider_0_1350.setDisabled(False)
        self.horizontalSlider_0_1360.setDisabled(False)
        self.horizontalSlider_0_1370.setDisabled(False)
        self.horizontalSlider_0_1300.setDisabled(False)
        self.horizontalSlider_0_1410.setDisabled(False)
        self.horizontalSlider_0_1420.setDisabled(False)
        self.horizontalSlider_0_1430.setDisabled(False)
        self.horizontalSlider_0_1450.setDisabled(False)
        self.horizontalSlider_0_1400.setDisabled(False)
        self.horizontalSlider_0_1510.setDisabled(False)
        self.horizontalSlider_0_1520.setDisabled(False)
        self.horizontalSlider_0_1530.setDisabled(False)
        self.horizontalSlider_0_1540.setDisabled(False)
        self.horizontalSlider_0_1550.setDisabled(False)
        self.horizontalSlider_0_1500.setDisabled(False)
        self.horizontalSlider_0_1700.setDisabled(False)
        self.horizontalSlider_0_2110.setDisabled(False)
        self.horizontalSlider_0_2120.setDisabled(False)
        self.horizontalSlider_0_2100.setDisabled(False)
        self.horizontalSlider_0_2210.setDisabled(False)
        self.horizontalSlider_0_2220.setDisabled(False)
        self.horizontalSlider_0_2200.setDisabled(False)
        self.horizontalSlider_0_2310.setDisabled(False)
        self.horizontalSlider_0_2320.setDisabled(False)
        self.horizontalSlider_0_2330.setDisabled(False)
        self.horizontalSlider_0_2340.setDisabled(False)
        self.horizontalSlider_0_2350.setDisabled(False)
        self.horizontalSlider_0_2300.setDisabled(False)
        self.horizontalSlider_0_2410.setDisabled(False)
        self.horizontalSlider_0_2421.setDisabled(False)
        self.horizontalSlider_0_2430.setDisabled(False)
        self.horizontalSlider_0_2450.setDisabled(False)
        self.horizontalSlider_0_2460.setDisabled(False)
        self.horizontalSlider_0_2400.setDisabled(False)
        #period_1
        self.horizontalSlider_1_1110.setDisabled(False)
        self.horizontalSlider_1_1120.setDisabled(False)
        self.horizontalSlider_1_1130.setDisabled(False)
        self.horizontalSlider_1_1140.setDisabled(False)
        self.horizontalSlider_1_1150.setDisabled(False)
        self.horizontalSlider_1_1160.setDisabled(False)
        self.horizontalSlider_1_1170.setDisabled(False)
        self.horizontalSlider_1_1180.setDisabled(False)
        self.horizontalSlider_1_1190.setDisabled(False)
        self.horizontalSlider_1_1100.setDisabled(False)
        self.horizontalSlider_1_1210.setDisabled(False)
        self.horizontalSlider_1_1220.setDisabled(False)
        self.horizontalSlider_1_1230.setDisabled(False)
        self.horizontalSlider_1_1240.setDisabled(False)
        self.horizontalSlider_1_1250.setDisabled(False)
        self.horizontalSlider_1_1260.setDisabled(False)
        self.horizontalSlider_1_1600.setDisabled(False)
        self.horizontalSlider_1_1200.setDisabled(False)
        self.horizontalSlider_1_1310.setDisabled(False)
        self.horizontalSlider_1_1320.setDisabled(False)
        self.horizontalSlider_1_1340.setDisabled(False)
        self.horizontalSlider_1_1350.setDisabled(False)
        self.horizontalSlider_1_1360.setDisabled(False)
        self.horizontalSlider_1_1370.setDisabled(False)
        self.horizontalSlider_1_1300.setDisabled(False)
        self.horizontalSlider_1_1410.setDisabled(False)
        self.horizontalSlider_1_1420.setDisabled(False)
        self.horizontalSlider_1_1430.setDisabled(False)
        self.horizontalSlider_1_1450.setDisabled(False)
        self.horizontalSlider_1_1400.setDisabled(False)
        self.horizontalSlider_1_1510.setDisabled(False)
        self.horizontalSlider_1_1520.setDisabled(False)
        self.horizontalSlider_1_1530.setDisabled(False)
        self.horizontalSlider_1_1540.setDisabled(False)
        self.horizontalSlider_1_1550.setDisabled(False)
        self.horizontalSlider_1_1500.setDisabled(False)
        self.horizontalSlider_1_1700.setDisabled(False)
        self.horizontalSlider_1_2110.setDisabled(False)
        self.horizontalSlider_1_2120.setDisabled(False)
        self.horizontalSlider_1_2100.setDisabled(False)
        self.horizontalSlider_1_2210.setDisabled(False)
        self.horizontalSlider_1_2220.setDisabled(False)
        self.horizontalSlider_1_2200.setDisabled(False)
        self.horizontalSlider_1_2310.setDisabled(False)
        self.horizontalSlider_1_2320.setDisabled(False)
        self.horizontalSlider_1_2330.setDisabled(False)
        self.horizontalSlider_1_2340.setDisabled(False)
        self.horizontalSlider_1_2350.setDisabled(False)
        self.horizontalSlider_1_2300.setDisabled(False)
        self.horizontalSlider_1_2410.setDisabled(False)
        self.horizontalSlider_1_2421.setDisabled(False)
        self.horizontalSlider_1_2430.setDisabled(False)
        self.horizontalSlider_1_2450.setDisabled(False)
        self.horizontalSlider_1_2460.setDisabled(False)
        self.horizontalSlider_1_2400.setDisabled(False)
        #period_2
        self.horizontalSlider_2_1110.setDisabled(False)
        self.horizontalSlider_2_1120.setDisabled(False)
        self.horizontalSlider_2_1130.setDisabled(False)
        self.horizontalSlider_2_1140.setDisabled(False)
        self.horizontalSlider_2_1150.setDisabled(False)
        self.horizontalSlider_2_1160.setDisabled(False)
        self.horizontalSlider_2_1170.setDisabled(False)
        self.horizontalSlider_2_1180.setDisabled(False)
        self.horizontalSlider_2_1190.setDisabled(False)
        self.horizontalSlider_2_1100.setDisabled(False)
        self.horizontalSlider_2_1210.setDisabled(False)
        self.horizontalSlider_2_1220.setDisabled(False)
        self.horizontalSlider_2_1230.setDisabled(False)
        self.horizontalSlider_2_1240.setDisabled(False)
        self.horizontalSlider_2_1250.setDisabled(False)
        self.horizontalSlider_2_1260.setDisabled(False)
        self.horizontalSlider_2_1600.setDisabled(False)
        self.horizontalSlider_2_1200.setDisabled(False)
        self.horizontalSlider_2_1310.setDisabled(False)
        self.horizontalSlider_2_1320.setDisabled(False)
        self.horizontalSlider_2_1340.setDisabled(False)
        self.horizontalSlider_2_1350.setDisabled(False)
        self.horizontalSlider_2_1360.setDisabled(False)
        self.horizontalSlider_2_1370.setDisabled(False)
        self.horizontalSlider_2_1300.setDisabled(False)
        self.horizontalSlider_2_1410.setDisabled(False)
        self.horizontalSlider_2_1420.setDisabled(False)
        self.horizontalSlider_2_1430.setDisabled(False)
        self.horizontalSlider_2_1450.setDisabled(False)
        self.horizontalSlider_2_1400.setDisabled(False)
        self.horizontalSlider_2_1510.setDisabled(False)
        self.horizontalSlider_2_1520.setDisabled(False)
        self.horizontalSlider_2_1530.setDisabled(False)
        self.horizontalSlider_2_1540.setDisabled(False)
        self.horizontalSlider_2_1550.setDisabled(False)
        self.horizontalSlider_2_1500.setDisabled(False)
        self.horizontalSlider_2_1700.setDisabled(False)
        self.horizontalSlider_2_2110.setDisabled(False)
        self.horizontalSlider_2_2120.setDisabled(False)
        self.horizontalSlider_2_2100.setDisabled(False)
        self.horizontalSlider_2_2210.setDisabled(False)
        self.horizontalSlider_2_2220.setDisabled(False)
        self.horizontalSlider_2_2200.setDisabled(False)
        self.horizontalSlider_2_2310.setDisabled(False)
        self.horizontalSlider_2_2320.setDisabled(False)
        self.horizontalSlider_2_2330.setDisabled(False)
        self.horizontalSlider_2_2340.setDisabled(False)
        self.horizontalSlider_2_2350.setDisabled(False)
        self.horizontalSlider_2_2300.setDisabled(False)
        self.horizontalSlider_2_2410.setDisabled(False)
        self.horizontalSlider_2_2421.setDisabled(False)
        self.horizontalSlider_2_2430.setDisabled(False)
        self.horizontalSlider_2_2450.setDisabled(False)
        self.horizontalSlider_2_2460.setDisabled(False)
        self.horizontalSlider_2_2400.setDisabled(False)
        #period_3
        self.horizontalSlider_3_1110.setDisabled(False)
        self.horizontalSlider_3_1120.setDisabled(False)
        self.horizontalSlider_3_1130.setDisabled(False)
        self.horizontalSlider_3_1140.setDisabled(False)
        self.horizontalSlider_3_1150.setDisabled(False)
        self.horizontalSlider_3_1160.setDisabled(False)
        self.horizontalSlider_3_1170.setDisabled(False)
        self.horizontalSlider_3_1180.setDisabled(False)
        self.horizontalSlider_3_1190.setDisabled(False)
        self.horizontalSlider_3_1100.setDisabled(False)
        self.horizontalSlider_3_1210.setDisabled(False)
        self.horizontalSlider_3_1220.setDisabled(False)
        self.horizontalSlider_3_1230.setDisabled(False)
        self.horizontalSlider_3_1240.setDisabled(False)
        self.horizontalSlider_3_1250.setDisabled(False)
        self.horizontalSlider_3_1260.setDisabled(False)
        self.horizontalSlider_3_1600.setDisabled(False)
        self.horizontalSlider_3_1200.setDisabled(False)
        self.horizontalSlider_3_1310.setDisabled(False)
        self.horizontalSlider_3_1320.setDisabled(False)
        self.horizontalSlider_3_1340.setDisabled(False)
        self.horizontalSlider_3_1350.setDisabled(False)
        self.horizontalSlider_3_1360.setDisabled(False)
        self.horizontalSlider_3_1370.setDisabled(False)
        self.horizontalSlider_3_1300.setDisabled(False)
        self.horizontalSlider_3_1410.setDisabled(False)
        self.horizontalSlider_3_1420.setDisabled(False)
        self.horizontalSlider_3_1430.setDisabled(False)
        self.horizontalSlider_3_1450.setDisabled(False)
        self.horizontalSlider_3_1400.setDisabled(False)
        self.horizontalSlider_3_1510.setDisabled(False)
        self.horizontalSlider_3_1520.setDisabled(False)
        self.horizontalSlider_3_1530.setDisabled(False)
        self.horizontalSlider_3_1540.setDisabled(False)
        self.horizontalSlider_3_1550.setDisabled(False)
        self.horizontalSlider_3_1500.setDisabled(False)
        self.horizontalSlider_3_1700.setDisabled(False)
        self.horizontalSlider_3_2110.setDisabled(False)
        self.horizontalSlider_3_2120.setDisabled(False)
        self.horizontalSlider_3_2100.setDisabled(False)
        self.horizontalSlider_3_2210.setDisabled(False)
        self.horizontalSlider_3_2220.setDisabled(False)
        self.horizontalSlider_3_2200.setDisabled(False)
        self.horizontalSlider_3_2310.setDisabled(False)
        self.horizontalSlider_3_2320.setDisabled(False)
        self.horizontalSlider_3_2330.setDisabled(False)
        self.horizontalSlider_3_2340.setDisabled(False)
        self.horizontalSlider_3_2350.setDisabled(False)
        self.horizontalSlider_3_2300.setDisabled(False)
        self.horizontalSlider_3_2410.setDisabled(False)
        self.horizontalSlider_3_2421.setDisabled(False)
        self.horizontalSlider_3_2430.setDisabled(False)
        self.horizontalSlider_3_2450.setDisabled(False)
        self.horizontalSlider_3_2460.setDisabled(False)
        self.horizontalSlider_3_2400.setDisabled(False)
        self.clear_lines()
def clear_lines(self):
    self.lineEdit_0_1110.clear()
    self.lineEdit_0_1120.clear()
    self.lineEdit_0_1130.clear()
    self.lineEdit_0_1140.clear()
    self.lineEdit_0_1150.clear()
    self.lineEdit_0_1160.clear()
    self.lineEdit_0_1170.clear()
    self.lineEdit_0_1180.clear()
    self.lineEdit_0_1190.clear()
    self.lineEdit_0_1100.clear()
    self.lineEdit_0_1210.clear()
    self.lineEdit_0_1220.clear()
    self.lineEdit_0_1230.clear()
    self.lineEdit_0_1240.clear()
    self.lineEdit_0_1250.clear()
    self.lineEdit_0_1260.clear()
    self.lineEdit_0_1200.clear()
    self.lineEdit_0_1600.clear()
    self.lineEdit_0_1310.clear()
    self.lineEdit_0_1320.clear()
    self.lineEdit_0_1340.clear()
    self.lineEdit_0_1350.clear()
    self.lineEdit_0_1360.clear()
    self.lineEdit_0_1370.clear()
    self.lineEdit_0_1300.clear()
    self.lineEdit_0_1410.clear()
    self.lineEdit_0_1420.clear()
    self.lineEdit_0_1430.clear()
    self.lineEdit_0_1450.clear()
    self.lineEdit_0_1400.clear()
    self.lineEdit_0_1510.clear()
    self.lineEdit_0_1520.clear()
    self.lineEdit_0_1530.clear()
    self.lineEdit_0_1540.clear()
    self.lineEdit_0_1550.clear()
    self.lineEdit_0_1500.clear()
    self.lineEdit_0_1700.clear()
    self.lineEdit_0_2110.clear()
    self.lineEdit_0_2120.clear()
    self.lineEdit_0_2100.clear()
    self.lineEdit_0_2210.clear()
    self.lineEdit_0_2220.clear()
    self.lineEdit_0_2200.clear()
    self.lineEdit_0_2310.clear()
    self.lineEdit_0_2320.clear()
    self.lineEdit_0_2330.clear()
    self.lineEdit_0_2340.clear()
    self.lineEdit_0_2350.clear()
    self.lineEdit_0_2300.clear()
    self.lineEdit_0_2410.clear()
    self.lineEdit_0_2421.clear()
    self.lineEdit_0_2430.clear()
    self.lineEdit_0_2450.clear()
    self.lineEdit_0_2460.clear()
    self.lineEdit_0_2400.clear()
    self.lineEdit_1_1110.clear()
    self.lineEdit_1_1120.clear()
    self.lineEdit_1_1130.clear()
    self.lineEdit_1_1140.clear()
    self.lineEdit_1_1150.clear()
    self.lineEdit_1_1160.clear()
    self.lineEdit_1_1170.clear()
    self.lineEdit_1_1180.clear()
    self.lineEdit_1_1190.clear()
    self.lineEdit_1_1100.clear()
    self.lineEdit_1_1210.clear()
    self.lineEdit_1_1220.clear()
    self.lineEdit_1_1230.clear()
    self.lineEdit_1_1240.clear()
    self.lineEdit_1_1250.clear()
    self.lineEdit_1_1260.clear()
    self.lineEdit_1_1200.clear()
    self.lineEdit_1_1600.clear()
    self.lineEdit_1_1310.clear()
    self.lineEdit_1_1320.clear()
    self.lineEdit_1_1340.clear()
    self.lineEdit_1_1350.clear()
    self.lineEdit_1_1360.clear()
    self.lineEdit_1_1370.clear()
    self.lineEdit_1_1300.clear()
    self.lineEdit_1_1410.clear()
    self.lineEdit_1_1420.clear()
    self.lineEdit_1_1430.clear()
    self.lineEdit_1_1450.clear()
    self.lineEdit_1_1400.clear()
    self.lineEdit_1_1510.clear()
    self.lineEdit_1_1520.clear()
    self.lineEdit_1_1530.clear()
    self.lineEdit_1_1540.clear()
    self.lineEdit_1_1550.clear()
    self.lineEdit_1_1500.clear()
    self.lineEdit_1_1700.clear()
    self.lineEdit_1_2110.clear()
    self.lineEdit_1_2120.clear()
    self.lineEdit_1_2100.clear()
    self.lineEdit_1_2210.clear()
    self.lineEdit_1_2220.clear()
    self.lineEdit_1_2200.clear()
    self.lineEdit_1_2310.clear()
    self.lineEdit_1_2320.clear()
    self.lineEdit_1_2330.clear()
    self.lineEdit_1_2340.clear()
    self.lineEdit_1_2350.clear()
    self.lineEdit_1_2300.clear()
    self.lineEdit_1_2410.clear()
    self.lineEdit_1_2421.clear()
    self.lineEdit_1_2430.clear()
    self.lineEdit_1_2450.clear()
    self.lineEdit_1_2460.clear()
    self.lineEdit_1_2400.clear()
    self.lineEdit_2_1110.clear()
    self.lineEdit_2_1120.clear()
    self.lineEdit_2_1130.clear()
    self.lineEdit_2_1140.clear()
    self.lineEdit_2_1150.clear()
    self.lineEdit_2_1160.clear()
    self.lineEdit_2_1170.clear()
    self.lineEdit_2_1180.clear()
    self.lineEdit_2_1190.clear()
    self.lineEdit_2_1100.clear()
    self.lineEdit_2_1210.clear()
    self.lineEdit_2_1220.clear()
    self.lineEdit_2_1230.clear()
    self.lineEdit_2_1240.clear()
    self.lineEdit_2_1250.clear()
    self.lineEdit_2_1260.clear()
    self.lineEdit_2_1200.clear()
    self.lineEdit_2_1600.clear()
    self.lineEdit_2_1310.clear()
    self.lineEdit_2_1320.clear()
    self.lineEdit_2_1340.clear()
    self.lineEdit_2_1350.clear()
    self.lineEdit_2_1360.clear()
    self.lineEdit_2_1370.clear()
    self.lineEdit_2_1300.clear()
    self.lineEdit_2_1410.clear()
    self.lineEdit_2_1420.clear()
    self.lineEdit_2_1430.clear()
    self.lineEdit_2_1450.clear()
    self.lineEdit_2_1400.clear()
    self.lineEdit_2_1510.clear()
    self.lineEdit_2_1520.clear()
    self.lineEdit_2_1530.clear()
    self.lineEdit_2_1540.clear()
    self.lineEdit_2_1550.clear()
    self.lineEdit_2_1500.clear()
    self.lineEdit_2_1700.clear()
    self.lineEdit_2_2110.clear()
    self.lineEdit_2_2120.clear()
    self.lineEdit_2_2100.clear()
    self.lineEdit_2_2210.clear()
    self.lineEdit_2_2220.clear()
    self.lineEdit_2_2200.clear()
    self.lineEdit_2_2310.clear()
    self.lineEdit_2_2320.clear()
    self.lineEdit_2_2330.clear()
    self.lineEdit_2_2340.clear()
    self.lineEdit_2_2350.clear()
    self.lineEdit_2_2300.clear()
    self.lineEdit_2_2410.clear()
    self.lineEdit_2_2421.clear()
    self.lineEdit_2_2430.clear()
    self.lineEdit_2_2450.clear()
    self.lineEdit_2_2460.clear()
    self.lineEdit_2_2400.clear()
    self.lineEdit_3_1110.clear()
    self.lineEdit_3_1120.clear()
    self.lineEdit_3_1130.clear()
    self.lineEdit_3_1140.clear()
    self.lineEdit_3_1150.clear()
    self.lineEdit_3_1160.clear()
    self.lineEdit_3_1170.clear()
    self.lineEdit_3_1180.clear()
    self.lineEdit_3_1190.clear()
    self.lineEdit_3_1100.clear()
    self.lineEdit_3_1210.clear()
    self.lineEdit_3_1220.clear()
    self.lineEdit_3_1230.clear()
    self.lineEdit_3_1240.clear()
    self.lineEdit_3_1250.clear()
    self.lineEdit_3_1260.clear()
    self.lineEdit_3_1200.clear()
    self.lineEdit_3_1600.clear()
    self.lineEdit_3_1310.clear()
    self.lineEdit_3_1320.clear()
    self.lineEdit_3_1340.clear()
    self.lineEdit_3_1350.clear()
    self.lineEdit_3_1360.clear()
    self.lineEdit_3_1370.clear()
    self.lineEdit_3_1300.clear()
    self.lineEdit_3_1410.clear()
    self.lineEdit_3_1420.clear()
    self.lineEdit_3_1430.clear()
    self.lineEdit_3_1450.clear()
    self.lineEdit_3_1400.clear()
    self.lineEdit_3_1510.clear()
    self.lineEdit_3_1520.clear()
    self.lineEdit_3_1530.clear()
    self.lineEdit_3_1540.clear()
    self.lineEdit_3_1550.clear()
    self.lineEdit_3_1500.clear()
    self.lineEdit_3_1700.clear()
    self.lineEdit_3_2110.clear()
    self.lineEdit_3_2120.clear()
    self.lineEdit_3_2100.clear()
    self.lineEdit_3_2210.clear()
    self.lineEdit_3_2220.clear()
    self.lineEdit_3_2200.clear()
    self.lineEdit_3_2310.clear()
    self.lineEdit_3_2320.clear()
    self.lineEdit_3_2330.clear()
    self.lineEdit_3_2340.clear()
    self.lineEdit_3_2350.clear()
    self.lineEdit_3_2300.clear()
    self.lineEdit_3_2410.clear()
    self.lineEdit_3_2421.clear()
    self.lineEdit_3_2430.clear()
    self.lineEdit_3_2450.clear()
    self.lineEdit_3_2460.clear()
    self.lineEdit_3_2400.clear()
def collect_data(self):
    if self.checkBox.isChecked():
        self.get_all_lines_text()
    else:
        self.get_all_slider_values()
    self.stats.current_liquidity()
    self.stats.fast_liquidity()
    self.stats.financial_independence()
    self.stats.leverage_ratio()
    self.stats.vis_cur_liq()
    self.stats.vis_fast_liq()
    self.stats.vis_abs_liq()
    self.stats.vis_fin_ind()
    self.stats.vis_lev_rat()
    self.stats.vis_work_cap()
    self.stats.vis_inv_rat()
    self.stats.vis_inv_per()
    self.stats.vis_rec_rat()
    self.stats.vis_rec_per()
    self.stats.vis_pay_rat()
    self.stats.vis_pay_per()
    self.stats.vis_oper_cyc()
    self.stats.vis_fin_cyc()
    self.stats.vis_roa()
    self.stats.vis_roe()
    self.stats.vis_ropfs()
    self.stats.vis_net_mar()
def get_all_slider_values(self):
    #period_0
    self.stats.balance[1110] = [self.horizontalSlider_0_1110.value()]
    self.stats.balance[1120] = [self.horizontalSlider_0_1120.value()]
    self.stats.balance[1130] = [self.horizontalSlider_0_1130.value()]
    self.stats.balance[1140] = [self.horizontalSlider_0_1140.value()]
    self.stats.balance[1150] = [self.horizontalSlider_0_1150.value()]
    self.stats.balance[1160] = [self.horizontalSlider_0_1160.value()]
    self.stats.balance[1170] = [self.horizontalSlider_0_1170.value()]
    self.stats.balance[1180] = [self.horizontalSlider_0_1180.value()]
    self.stats.balance[1190] = [self.horizontalSlider_0_1190.value()]
    self.stats.balance[1100] = [self.horizontalSlider_0_1100.value()]
    self.stats.balance[1110].append(self.horizontalSlider_1_1110.value())
    self.stats.balance[1120].append(self.horizontalSlider_1_1120.value())
    self.stats.balance[1130].append(self.horizontalSlider_1_1130.value())
    self.stats.balance[1140].append(self.horizontalSlider_1_1140.value())
    self.stats.balance[1150].append(self.horizontalSlider_1_1150.value())
    self.stats.balance[1160].append(self.horizontalSlider_1_1160.value())
    self.stats.balance[1170].append(self.horizontalSlider_1_1170.value())
    self.stats.balance[1180].append(self.horizontalSlider_1_1180.value())
    self.stats.balance[1190].append(self.horizontalSlider_1_1190.value())
    self.stats.balance[1100].append(self.horizontalSlider_1_1100.value())
    self.stats.balance[1110].append(self.horizontalSlider_2_1110.value())
    self.stats.balance[1120].append(self.horizontalSlider_2_1120.value())
    self.stats.balance[1130].append(self.horizontalSlider_2_1130.value())
    self.stats.balance[1140].append(self.horizontalSlider_2_1140.value())
    self.stats.balance[1150].append(self.horizontalSlider_2_1150.value())
    self.stats.balance[1160].append(self.horizontalSlider_2_1160.value())
    self.stats.balance[1170].append(self.horizontalSlider_2_1170.value())
    self.stats.balance[1180].append(self.horizontalSlider_2_1180.value())
    self.stats.balance[1190].append(self.horizontalSlider_2_1190.value())
    self.stats.balance[1100].append(self.horizontalSlider_2_1100.value())
    self.stats.balance[1110].append(self.horizontalSlider_3_1110.value())
    self.stats.balance[1120].append(self.horizontalSlider_3_1120.value())
    self.stats.balance[1130].append(self.horizontalSlider_3_1130.value())
    self.stats.balance[1140].append(self.horizontalSlider_3_1140.value())
    self.stats.balance[1150].append(self.horizontalSlider_3_1150.value())
    self.stats.balance[1160].append(self.horizontalSlider_3_1160.value())
    self.stats.balance[1170].append(self.horizontalSlider_3_1170.value())
    self.stats.balance[1180].append(self.horizontalSlider_3_1180.value())
    self.stats.balance[1190].append(self.horizontalSlider_3_1190.value())
    self.stats.balance[1100].append(self.horizontalSlider_3_1100.value())
    self.stats.balance[1210] = [self.horizontalSlider_0_1210.value()]
    self.stats.balance[1220] = [self.horizontalSlider_0_1220.value()]
    self.stats.balance[1230] = [self.horizontalSlider_0_1230.value()]
    self.stats.balance[1240] = [self.horizontalSlider_0_1240.value()]
    self.stats.balance[1250] = [self.horizontalSlider_0_1250.value()]
    self.stats.balance[1260] = [self.horizontalSlider_0_1260.value()]
    self.stats.balance[1200] = [self.horizontalSlider_0_1200.value()]
    self.stats.balance[1600] = [self.horizontalSlider_0_1600.value()]
    self.stats.balance[1210].append(self.horizontalSlider_1_1210.value())
    self.stats.balance[1220].append(self.horizontalSlider_1_1220.value())
    self.stats.balance[1230].append(self.horizontalSlider_1_1230.value())
    self.stats.balance[1240].append(self.horizontalSlider_1_1240.value())
    self.stats.balance[1250].append(self.horizontalSlider_1_1250.value())
    self.stats.balance[1260].append(self.horizontalSlider_1_1260.value())
    self.stats.balance[1200].append(self.horizontalSlider_1_1200.value())
    self.stats.balance[1600].append(self.horizontalSlider_1_1600.value())
    self.stats.balance[1210].append(self.horizontalSlider_2_1210.value())
    self.stats.balance[1220].append(self.horizontalSlider_2_1220.value())
    self.stats.balance[1230].append(self.horizontalSlider_2_1230.value())
    self.stats.balance[1240].append(self.horizontalSlider_2_1240.value())
    self.stats.balance[1250].append(self.horizontalSlider_2_1250.value())
    self.stats.balance[1260].append(self.horizontalSlider_2_1260.value())
    self.stats.balance[1200].append(self.horizontalSlider_2_1200.value())
    self.stats.balance[1600].append(self.horizontalSlider_2_1600.value())
    self.stats.balance[1210].append(self.horizontalSlider_3_1210.value())
    self.stats.balance[1220].append(self.horizontalSlider_3_1220.value())
    self.stats.balance[1230].append(self.horizontalSlider_3_1230.value())
    self.stats.balance[1240].append(self.horizontalSlider_3_1240.value())
    self.stats.balance[1250].append(self.horizontalSlider_3_1250.value())
    self.stats.balance[1260].append(self.horizontalSlider_3_1260.value())
    self.stats.balance[1200].append(self.horizontalSlider_3_1200.value())
    self.stats.balance[1600].append(self.horizontalSlider_3_1600.value())
    self.stats.balance[1310] = [self.horizontalSlider_0_1310.value()]
    self.stats.balance[1320] = [self.horizontalSlider_0_1320.value()]
    self.stats.balance[1340] = [self.horizontalSlider_0_1340.value()]
    self.stats.balance[1350] = [self.horizontalSlider_0_1350.value()]
    self.stats.balance[1360] = [self.horizontalSlider_0_1360.value()]
    self.stats.balance[1370] = [self.horizontalSlider_0_1370.value()]
    self.stats.balance[1300] = [self.horizontalSlider_0_1300.value()]
    self.stats.balance[1410] = [self.horizontalSlider_0_1410.value()]
    self.stats.balance[1420] = [self.horizontalSlider_0_1420.value()]
    self.stats.balance[1430] = [self.horizontalSlider_0_1430.value()]
    self.stats.balance[1450] = [self.horizontalSlider_0_1450.value()]
    self.stats.balance[1400] = [self.horizontalSlider_0_1400.value()]
    self.stats.balance[1510] = [self.horizontalSlider_0_1510.value()]
    self.stats.balance[1520] = [self.horizontalSlider_0_1520.value()]
    self.stats.balance[1530] = [self.horizontalSlider_0_1530.value()]
    self.stats.balance[1540] = [self.horizontalSlider_0_1540.value()]
    self.stats.balance[1550] = [self.horizontalSlider_0_1550.value()]
    self.stats.balance[1500] = [self.horizontalSlider_0_1500.value()]
    self.stats.balance[1700] = [self.horizontalSlider_0_1700.value()]
    self.stats.balance[1310].append(self.horizontalSlider_1_1310.value())
    self.stats.balance[1320].append(self.horizontalSlider_1_1320.value())
    self.stats.balance[1340].append(self.horizontalSlider_1_1340.value())
    self.stats.balance[1350].append(self.horizontalSlider_1_1350.value())
    self.stats.balance[1360].append(self.horizontalSlider_1_1360.value())
    self.stats.balance[1370].append(self.horizontalSlider_1_1370.value())
    self.stats.balance[1300].append(self.horizontalSlider_1_1310.value())
    self.stats.balance[1410].append(self.horizontalSlider_1_1410.value())
    self.stats.balance[1420].append(self.horizontalSlider_1_1420.value())
    self.stats.balance[1430].append(self.horizontalSlider_1_1430.value())
    self.stats.balance[1450].append(self.horizontalSlider_1_1450.value())
    self.stats.balance[1400].append(self.horizontalSlider_1_1400.value())
    self.stats.balance[1510].append(self.horizontalSlider_1_1510.value())
    self.stats.balance[1520].append(self.horizontalSlider_1_1520.value())
    self.stats.balance[1530].append(self.horizontalSlider_1_1530.value())
    self.stats.balance[1540].append(self.horizontalSlider_1_1540.value())
    self.stats.balance[1550].append(self.horizontalSlider_1_1550.value())
    self.stats.balance[1500].append(self.horizontalSlider_1_1500.value())
    self.stats.balance[1700].append(self.horizontalSlider_1_1700.value())
    self.stats.balance[1310].append(self.horizontalSlider_2_1310.value())
    self.stats.balance[1320].append(self.horizontalSlider_2_1320.value())
    self.stats.balance[1340].append(self.horizontalSlider_2_1340.value())
    self.stats.balance[1350].append(self.horizontalSlider_2_1350.value())
    self.stats.balance[1360].append(self.horizontalSlider_2_1360.value())
    self.stats.balance[1370].append(self.horizontalSlider_2_1370.value())
    self.stats.balance[1300].append(self.horizontalSlider_2_1310.value())
    self.stats.balance[1410].append(self.horizontalSlider_2_1410.value())
    self.stats.balance[1420].append(self.horizontalSlider_2_1420.value())
    self.stats.balance[1430].append(self.horizontalSlider_2_1430.value())
    self.stats.balance[1450].append(self.horizontalSlider_2_1450.value())
    self.stats.balance[1400].append(self.horizontalSlider_2_1400.value())
    self.stats.balance[1510].append(self.horizontalSlider_2_1510.value())
    self.stats.balance[1520].append(self.horizontalSlider_2_1520.value())
    self.stats.balance[1530].append(self.horizontalSlider_2_1530.value())
    self.stats.balance[1540].append(self.horizontalSlider_2_1540.value())
    self.stats.balance[1550].append(self.horizontalSlider_2_1550.value())
    self.stats.balance[1500].append(self.horizontalSlider_2_1500.value())
    self.stats.balance[1700].append(self.horizontalSlider_2_1700.value())
    self.stats.balance[1310].append(self.horizontalSlider_3_1310.value())
    self.stats.balance[1320].append(self.horizontalSlider_3_1320.value())
    self.stats.balance[1340].append(self.horizontalSlider_3_1340.value())
    self.stats.balance[1350].append(self.horizontalSlider_3_1350.value())
    self.stats.balance[1360].append(self.horizontalSlider_3_1360.value())
    self.stats.balance[1370].append(self.horizontalSlider_3_1370.value())
    self.stats.balance[1300].append(self.horizontalSlider_3_1310.value())
    self.stats.balance[1410].append(self.horizontalSlider_3_1410.value())
    self.stats.balance[1420].append(self.horizontalSlider_3_1420.value())
    self.stats.balance[1430].append(self.horizontalSlider_3_1430.value())
    self.stats.balance[1450].append(self.horizontalSlider_3_1450.value())
    self.stats.balance[1400].append(self.horizontalSlider_3_1400.value())
    self.stats.balance[1510].append(self.horizontalSlider_3_1510.value())
    self.stats.balance[1520].append(self.horizontalSlider_3_1520.value())
    self.stats.balance[1530].append(self.horizontalSlider_3_1530.value())
    self.stats.balance[1540].append(self.horizontalSlider_3_1540.value())
    self.stats.balance[1550].append(self.horizontalSlider_3_1550.value())
    self.stats.balance[1500].append(self.horizontalSlider_3_1500.value())
    self.stats.balance[1700].append(self.horizontalSlider_3_1700.value())
    for i in self.stats.balance:
        print(i, self.stats.balance[i])
    print()
    #ofr
    #period_0
    self.stats.ofr[2110] = [self.horizontalSlider_0_2110.value()]
    self.stats.ofr[2120] = [self.horizontalSlider_0_2120.value()]
    self.stats.ofr[2100] = [self.horizontalSlider_0_2100.value()]
    self.stats.ofr[2210] = [self.horizontalSlider_0_2210.value()]
    self.stats.ofr[2220] = [self.horizontalSlider_0_2220.value()]
    self.stats.ofr[2200] = [self.horizontalSlider_0_2200.value()]
    self.stats.ofr[2310] = [self.horizontalSlider_0_2310.value()]
    self.stats.ofr[2320] = [self.horizontalSlider_0_2320.value()]
    self.stats.ofr[2330] = [self.horizontalSlider_0_2330.value()]
    self.stats.ofr[2340] = [self.horizontalSlider_0_2340.value()]
    self.stats.ofr[2350] = [self.horizontalSlider_0_2350.value()]
    self.stats.ofr[2300] = [self.horizontalSlider_0_2300.value()]
    self.stats.ofr[2410] = [self.horizontalSlider_0_2410.value()]
    self.stats.ofr[2421] = [self.horizontalSlider_0_2421.value()]
    self.stats.ofr[2430] = [self.horizontalSlider_0_2430.value()]
    self.stats.ofr[2450] = [self.horizontalSlider_0_2450.value()]
    self.stats.ofr[2460] = [self.horizontalSlider_0_2460.value()]
    self.stats.ofr[2400] = [self.horizontalSlider_0_2400.value()]
    self.stats.ofr[2110].append(self.horizontalSlider_1_2110.value())
    self.stats.ofr[2120].append(self.horizontalSlider_1_2120.value())
    self.stats.ofr[2100].append(self.horizontalSlider_1_2100.value())
    self.stats.ofr[2210].append(self.horizontalSlider_1_2210.value())
    self.stats.ofr[2220].append(self.horizontalSlider_1_2220.value())
    self.stats.ofr[2200].append(self.horizontalSlider_1_2200.value())
    self.stats.ofr[2310].append(self.horizontalSlider_1_2310.value())
    self.stats.ofr[2320].append(self.horizontalSlider_1_2320.value())
    self.stats.ofr[2330].append(self.horizontalSlider_1_2330.value())
    self.stats.ofr[2340].append(self.horizontalSlider_1_2340.value())
    self.stats.ofr[2350].append(self.horizontalSlider_1_2350.value())
    self.stats.ofr[2300].append(self.horizontalSlider_1_2300.value())
    self.stats.ofr[2410].append(self.horizontalSlider_1_2410.value())
    self.stats.ofr[2421].append(self.horizontalSlider_1_2421.value())
    self.stats.ofr[2430].append(self.horizontalSlider_1_2430.value())
    self.stats.ofr[2450].append(self.horizontalSlider_1_2450.value())
    self.stats.ofr[2460].append(self.horizontalSlider_1_2460.value())
    self.stats.ofr[2400].append(self.horizontalSlider_1_2400.value())
    self.stats.ofr[2110].append(self.horizontalSlider_2_2110.value())
    self.stats.ofr[2120].append(self.horizontalSlider_2_2120.value())
    self.stats.ofr[2100].append(self.horizontalSlider_2_2100.value())
    self.stats.ofr[2210].append(self.horizontalSlider_2_2210.value())
    self.stats.ofr[2220].append(self.horizontalSlider_2_2220.value())
    self.stats.ofr[2200].append(self.horizontalSlider_2_2200.value())
    self.stats.ofr[2310].append(self.horizontalSlider_2_2310.value())
    self.stats.ofr[2320].append(self.horizontalSlider_2_2320.value())
    self.stats.ofr[2330].append(self.horizontalSlider_2_2330.value())
    self.stats.ofr[2340].append(self.horizontalSlider_2_2340.value())
    self.stats.ofr[2350].append(self.horizontalSlider_2_2350.value())
    self.stats.ofr[2300].append(self.horizontalSlider_2_2300.value())
    self.stats.ofr[2410].append(self.horizontalSlider_2_2410.value())
    self.stats.ofr[2421].append(self.horizontalSlider_2_2421.value())
    self.stats.ofr[2430].append(self.horizontalSlider_2_2430.value())
    self.stats.ofr[2450].append(self.horizontalSlider_2_2450.value())
    self.stats.ofr[2460].append(self.horizontalSlider_2_2460.value())
    self.stats.ofr[2400].append(self.horizontalSlider_2_2400.value())
    self.stats.ofr[2110].append(self.horizontalSlider_3_2110.value())
    self.stats.ofr[2120].append(self.horizontalSlider_3_2120.value())
    self.stats.ofr[2100].append(self.horizontalSlider_3_2100.value())
    self.stats.ofr[2210].append(self.horizontalSlider_3_2210.value())
    self.stats.ofr[2220].append(self.horizontalSlider_3_2220.value())
    self.stats.ofr[2200].append(self.horizontalSlider_3_2200.value())
    self.stats.ofr[2310].append(self.horizontalSlider_3_2310.value())
    self.stats.ofr[2320].append(self.horizontalSlider_3_2320.value())
    self.stats.ofr[2330].append(self.horizontalSlider_3_2330.value())
    self.stats.ofr[2340].append(self.horizontalSlider_3_2340.value())
    self.stats.ofr[2350].append(self.horizontalSlider_3_2350.value())
    self.stats.ofr[2300].append(self.horizontalSlider_3_2300.value())
    self.stats.ofr[2410].append(self.horizontalSlider_3_2410.value())
    self.stats.ofr[2421].append(self.horizontalSlider_3_2421.value())
    self.stats.ofr[2430].append(self.horizontalSlider_3_2430.value())
    self.stats.ofr[2450].append(self.horizontalSlider_3_2450.value())
    self.stats.ofr[2460].append(self.horizontalSlider_3_2460.value())
    self.stats.ofr[2400].append(self.horizontalSlider_3_2400.value())
    for i in self.stats.ofr:
        print(i, self.stats.ofr[i])
    print()
def get_all_lines_text(self):
    #0
    if self.lineEdit_0_1110.text():
        self.stats.balance[1110] = [int(self.lineEdit_0_1110.text())]
    else:
        self.stats.balance[1110] = [0]
    if self.lineEdit_0_1120.text():
        self.stats.balance[1120] = [int(self.lineEdit_0_1120.text())]
    else:
        self.stats.balance[1120] = [0]
    if self.lineEdit_0_1130.text():
        self.stats.balance[1130] = [int(self.lineEdit_0_1130.text())]
    else:
        self.stats.balance[1130] = [0]
    if self.lineEdit_0_1140.text():
        self.stats.balance[1140] = [int(self.lineEdit_0_1140.text())]
    else:
        self.stats.balance[1140] = [0]
    if self.lineEdit_0_1150.text():
        self.stats.balance[1150] = [int(self.lineEdit_0_1150.text())]
    else:
        self.stats.balance[1150] = [0]
    if self.lineEdit_0_1160.text():
        self.stats.balance[1160] = [int(self.lineEdit_0_1160.text())]
    else:
        self.stats.balance[1160] = [0]
    if self.lineEdit_0_1170.text():
        self.stats.balance[1170] = [int(self.lineEdit_0_1170.text())]
    else:
        self.stats.balance[1170] = [0]
    if self.lineEdit_0_1180.text():
        self.stats.balance[1180] = [int(self.lineEdit_0_1180.text())]
    else:
        self.stats.balance[1180] = [0]
    if self.lineEdit_0_1190.text():
        self.stats.balance[1190] = [int(self.lineEdit_0_1190.text())]
    else:
        self.stats.balance[1190] = [0]
    if self.lineEdit_0_1100.text():
        self.stats.balance[1100] = [int(self.lineEdit_0_1100.text())]
    else:
        self.stats.balance[1100] = [0]
    if self.lineEdit_0_1210.text():
        self.stats.balance[1210] = [int(self.lineEdit_0_1210.text())]
    else:
        self.stats.balance[1210] = [0]
    if self.lineEdit_0_1220.text():
        self.stats.balance[1220] = [int(self.lineEdit_0_1220.text())]
    else:
        self.stats.balance[1220] = [0]
    if self.lineEdit_0_1230.text():
        self.stats.balance[1230] = [int(self.lineEdit_0_1230.text())]
    else:
        self.stats.balance[1230] = [0]
    if self.lineEdit_0_1240.text():
        self.stats.balance[1240] = [int(self.lineEdit_0_1240.text())]
    else:
        self.stats.balance[1240] = [0]
    if self.lineEdit_0_1250.text():
        self.stats.balance[1250] = [int(self.lineEdit_0_1250.text())]
    else:
        self.stats.balance[1250] = [0]
    if self.lineEdit_0_1260.text():
        self.stats.balance[1260] = [int(self.lineEdit_0_1260.text())]
    else:
        self.stats.balance[1260] = [0]
    if self.lineEdit_0_1200.text():
        self.stats.balance[1200] = [int(self.lineEdit_0_1200.text())]
    else:
        self.stats.balance[1200] = [0]
    if self.lineEdit_0_1600.text():
        self.stats.balance[1600] = [int(self.lineEdit_0_1600.text())]
    else:
        self.stats.balance[1600] = [0]
    #пассив
    if self.lineEdit_0_1310.text():
        self.stats.balance[1310] = [int(self.lineEdit_0_1310.text())]
    else:
        self.stats.balance[1310] = [0]
    if self.lineEdit_0_1320.text():
        self.stats.balance[1320] = [int(self.lineEdit_0_1320.text())]
    else:
        self.stats.balance[1320] = [0]
    if self.lineEdit_0_1340.text():
        self.stats.balance[1340] = [int(self.lineEdit_0_1340.text())]
    else:
        self.stats.balance[1340] = [0]
    if self.lineEdit_0_1350.text():
        self.stats.balance[1350] = [int(self.lineEdit_0_1350.text())]
    else:
        self.stats.balance[1350] = [0]
    if self.lineEdit_0_1360.text():
        self.stats.balance[1360] = [int(self.lineEdit_0_1360.text())]
    else:
        self.stats.balance[1360] = [0]
    if self.lineEdit_0_1370.text():
        self.stats.balance[1370] = [int(self.lineEdit_0_1370.text())]
    else:
        self.stats.balance[1370] = [0]
    if self.lineEdit_0_1300.text():
        self.stats.balance[1300] = [int(self.lineEdit_0_1300.text())]
    else:
        self.stats.balance[1300] = [0]
    if self.lineEdit_0_1410.text():
        self.stats.balance[1410] = [int(self.lineEdit_0_1410.text())]
    else:
        self.stats.balance[1410] = [0]
    if self.lineEdit_0_1420.text():
        self.stats.balance[1420] = [int(self.lineEdit_0_1420.text())]
    else:
        self.stats.balance[1420] = [0]
    if self.lineEdit_0_1430.text():
        self.stats.balance[1430] = [int(self.lineEdit_0_1430.text())]
    else:
        self.stats.balance[1430] = [0]
    if self.lineEdit_0_1450.text():
        self.stats.balance[1450] = [int(self.lineEdit_0_1450.text())]
    else:
        self.stats.balance[1450] = [0]
    if self.lineEdit_0_1400.text():
        self.stats.balance[1400] = [int(self.lineEdit_0_1400.text())]
    else:
        self.stats.balance[1400] = [0]
    if self.lineEdit_0_1510.text():
        self.stats.balance[1510] = [int(self.lineEdit_0_1510.text())]
    else:
        self.stats.balance[1510] = [0]
    if self.lineEdit_0_1520.text():
        self.stats.balance[1520] = [int(self.lineEdit_0_1520.text())]
    else:
        self.stats.balance[1520] = [0]
    if self.lineEdit_0_1530.text():
        self.stats.balance[1530] = [int(self.lineEdit_0_1530.text())]
    else:
        self.stats.balance[1530] = [0]
    if self.lineEdit_0_1540.text():
        self.stats.balance[1540] = [int(self.lineEdit_0_1540.text())]
    else:
        self.stats.balance[1540] = [0]
    if self.lineEdit_0_1550.text():
        self.stats.balance[1550] = [int(self.lineEdit_0_1550.text())]
    else:
        self.stats.balance[1550] = [0]
    if self.lineEdit_0_1500.text():
        self.stats.balance[1500] = [int(self.lineEdit_0_1500.text())]
    else:
        self.stats.balance[1500] = [0]
    if self.lineEdit_0_1700.text():
        self.stats.balance[1700] = [int(self.lineEdit_0_1700.text())]
    else:
        self.stats.balance[1700] = [0]
    #1
    if self.lineEdit_1_1110.text():
        self.stats.balance[1110].append(int(self.lineEdit_1_1110.text()))
    else:
        self.stats.balance[1110].append(0)
    if self.lineEdit_1_1120.text():
        self.stats.balance[1120].append(int(self.lineEdit_1_1120.text()))
    else:
        self.stats.balance[1120].append(0)
    if self.lineEdit_1_1130.text():
        self.stats.balance[1130].append(int(self.lineEdit_1_1130.text()))
    else:
        self.stats.balance[1130].append(0)
    if self.lineEdit_1_1140.text():
        self.stats.balance[1140].append(int(self.lineEdit_1_1140.text()))
    else:
        self.stats.balance[1140].append(0)
    if self.lineEdit_1_1150.text():
        self.stats.balance[1150].append(int(self.lineEdit_1_1150.text()))
    else:
        self.stats.balance[1150].append(0)
    if self.lineEdit_1_1160.text():
        self.stats.balance[1160].append(int(self.lineEdit_1_1160.text()))
    else:
        self.stats.balance[1160].append(0)
    if self.lineEdit_1_1170.text():
        self.stats.balance[1170].append(int(self.lineEdit_1_1170.text()))
    else:
        self.stats.balance[1170].append(0)
    if self.lineEdit_1_1180.text():
        self.stats.balance[1180].append(int(self.lineEdit_1_1180.text()))
    else:
        self.stats.balance[1180].append(0)
    if self.lineEdit_1_1190.text():
        self.stats.balance[1190].append(int(self.lineEdit_1_1190.text()))
    else:
        self.stats.balance[1190].append(0)
    if self.lineEdit_1_1100.text():
        self.stats.balance[1100].append(int(self.lineEdit_1_1100.text()))
    else:
        self.stats.balance[1100].append(0)
    if self.lineEdit_1_1210.text():
        self.stats.balance[1210].append(int(self.lineEdit_1_1210.text()))
    else:
        self.stats.balance[1210].append(0)
    if self.lineEdit_1_1220.text():
        self.stats.balance[1220].append(int(self.lineEdit_1_1220.text()))
    else:
        self.stats.balance[1220].append(0)
    if self.lineEdit_1_1230.text():
        self.stats.balance[1230].append(int(self.lineEdit_1_1230.text()))
    else:
        self.stats.balance[1230].append(0)
    if self.lineEdit_1_1240.text():
        self.stats.balance[1240].append(int(self.lineEdit_1_1240.text()))
    else:
        self.stats.balance[1240].append(0)
    if self.lineEdit_1_1250.text():
        self.stats.balance[1250].append(int(self.lineEdit_1_1250.text()))
    else:
        self.stats.balance[1250].append(0)
    if self.lineEdit_1_1260.text():
        self.stats.balance[1260].append(int(self.lineEdit_1_1260.text()))
    else:
        self.stats.balance[1260].append(0)
    if self.lineEdit_1_1200.text():
        self.stats.balance[1200].append(int(self.lineEdit_1_1200.text()))
    else:
        self.stats.balance[1200].append(0)
    if self.lineEdit_1_1600.text():
        self.stats.balance[1600].append(int(self.lineEdit_1_1600.text()))
    else:
        self.stats.balance[1600].append(0)
    #пассив
    if self.lineEdit_1_1310.text():
        self.stats.balance[1310].append(int(self.lineEdit_1_1310.text()))
    else:
        self.stats.balance[1310].append(0)
    if self.lineEdit_1_1320.text():
        self.stats.balance[1320].append(int(self.lineEdit_1_1320.text()))
    else:
        self.stats.balance[1320].append(0)
    if self.lineEdit_1_1340.text():
        self.stats.balance[1340].append(int(self.lineEdit_1_1340.text()))
    else:
        self.stats.balance[1340].append(0)
    if self.lineEdit_1_1350.text():
        self.stats.balance[1350].append(int(self.lineEdit_1_1350.text()))
    else:
        self.stats.balance[1350].append(0)
    if self.lineEdit_1_1360.text():
        self.stats.balance[1360].append(int(self.lineEdit_1_1360.text()))
    else:
        self.stats.balance[1360].append(0)
    if self.lineEdit_1_1370.text():
        self.stats.balance[1370].append(int(self.lineEdit_1_1370.text()))
    else:
        self.stats.balance[1370].append(0)
    if self.lineEdit_1_1300.text():
        self.stats.balance[1300].append(int(self.lineEdit_1_1300.text()))
    else:
        self.stats.balance[1300].append(0)
    if self.lineEdit_1_1410.text():
        self.stats.balance[1410].append(int(self.lineEdit_1_1410.text()))
    else:
        self.stats.balance[1410].append(0)
    if self.lineEdit_1_1420.text():
        self.stats.balance[1420].append(int(self.lineEdit_1_1420.text()))
    else:
        self.stats.balance[1420].append(0)
    if self.lineEdit_1_1430.text():
        self.stats.balance[1430].append(int(self.lineEdit_1_1430.text()))
    else:
        self.stats.balance[1430].append(0)
    if self.lineEdit_1_1450.text():
        self.stats.balance[1450].append(int(self.lineEdit_1_1450.text()))
    else:
        self.stats.balance[1450].append(0)
    if self.lineEdit_1_1400.text():
        self.stats.balance[1400].append(int(self.lineEdit_1_1400.text()))
    else:
        self.stats.balance[1400].append(0)
    if self.lineEdit_1_1510.text():
        self.stats.balance[1510].append(int(self.lineEdit_1_1510.text()))
    else:
        self.stats.balance[1510].append(0)
    if self.lineEdit_1_1520.text():
        self.stats.balance[1520].append(int(self.lineEdit_1_1520.text()))
    else:
        self.stats.balance[1520].append(0)
    if self.lineEdit_1_1530.text():
        self.stats.balance[1530].append(int(self.lineEdit_1_1530.text()))
    else:
        self.stats.balance[1530].append(0)
    if self.lineEdit_1_1540.text():
        self.stats.balance[1540].append(int(self.lineEdit_1_1540.text()))
    else:
        self.stats.balance[1540].append(0)
    if self.lineEdit_1_1550.text():
        self.stats.balance[1550].append(int(self.lineEdit_1_1550.text()))
    else:
        self.stats.balance[1550].append(0)
    if self.lineEdit_1_1500.text():
        self.stats.balance[1500].append(int(self.lineEdit_1_1500.text()))
    else:
        self.stats.balance[1500].append(0)
    if self.lineEdit_1_1700.text():
        self.stats.balance[1700].append(int(self.lineEdit_1_1700.text()))
    else:
        self.stats.balance[1700].append(0)
    #2
    if self.lineEdit_2_1110.text():
        self.stats.balance[1110].append(int(self.lineEdit_2_1110.text()))
    else:
        self.stats.balance[1110].append(0)
    if self.lineEdit_2_1120.text():
        self.stats.balance[1120].append(int(self.lineEdit_2_1120.text()))
    else:
        self.stats.balance[1120].append(0)
    if self.lineEdit_2_1130.text():
        self.stats.balance[1130].append(int(self.lineEdit_2_1130.text()))
    else:
        self.stats.balance[1130].append(0)
    if self.lineEdit_2_1140.text():
        self.stats.balance[1140].append(int(self.lineEdit_2_1140.text()))
    else:
        self.stats.balance[1140].append(0)
    if self.lineEdit_2_1150.text():
        self.stats.balance[1150].append(int(self.lineEdit_2_1150.text()))
    else:
        self.stats.balance[1150].append(0)
    if self.lineEdit_2_1160.text():
        self.stats.balance[1160].append(int(self.lineEdit_2_1160.text()))
    else:
        self.stats.balance[1160].append(0)
    if self.lineEdit_2_1170.text():
        self.stats.balance[1170].append(int(self.lineEdit_2_1170.text()))
    else:
        self.stats.balance[1170].append(0)
    if self.lineEdit_2_1180.text():
        self.stats.balance[1180].append(int(self.lineEdit_2_1180.text()))
    else:
        self.stats.balance[1180].append(0)
    if self.lineEdit_2_1190.text():
        self.stats.balance[1190].append(int(self.lineEdit_2_1190.text()))
    else:
        self.stats.balance[1190].append(0)
    if self.lineEdit_2_1100.text():
        self.stats.balance[1100].append(int(self.lineEdit_2_1100.text()))
    else:
        self.stats.balance[1100].append(0)
    if self.lineEdit_2_1210.text():
        self.stats.balance[1210].append(int(self.lineEdit_2_1210.text()))
    else:
        self.stats.balance[1210].append(0)
    if self.lineEdit_2_1220.text():
        self.stats.balance[1220].append(int(self.lineEdit_2_1220.text()))
    else:
        self.stats.balance[1220].append(0)
    if self.lineEdit_2_1230.text():
        self.stats.balance[1230].append(int(self.lineEdit_2_1230.text()))
    else:
        self.stats.balance[1230].append(0)
    if self.lineEdit_2_1240.text():
        self.stats.balance[1240].append(int(self.lineEdit_2_1240.text()))
    else:
        self.stats.balance[1240].append(0)
    if self.lineEdit_2_1250.text():
        self.stats.balance[1250].append(int(self.lineEdit_2_1250.text()))
    else:
        self.stats.balance[1250].append(0)
    if self.lineEdit_2_1260.text():
        self.stats.balance[1260].append(int(self.lineEdit_2_1260.text()))
    else:
        self.stats.balance[1260].append(0)
    if self.lineEdit_2_1200.text():
        self.stats.balance[1200].append(int(self.lineEdit_2_1200.text()))
    else:
        self.stats.balance[1200].append(0)
    if self.lineEdit_2_1600.text():
        self.stats.balance[1600].append(int(self.lineEdit_2_1600.text()))
    else:
        self.stats.balance[1600].append(0)
    # пассив
    if self.lineEdit_2_1310.text():
        self.stats.balance[1310].append(int(self.lineEdit_2_1310.text()))
    else:
        self.stats.balance[1310].append(0)
    if self.lineEdit_2_1320.text():
        self.stats.balance[1320].append(int(self.lineEdit_2_1320.text()))
    else:
        self.stats.balance[1320].append(0)
    if self.lineEdit_2_1340.text():
        self.stats.balance[1340].append(int(self.lineEdit_2_1340.text()))
    else:
        self.stats.balance[1340].append(0)
    if self.lineEdit_2_1350.text():
        self.stats.balance[1350].append(int(self.lineEdit_2_1350.text()))
    else:
        self.stats.balance[1350].append(0)
    if self.lineEdit_2_1360.text():
        self.stats.balance[1360].append(int(self.lineEdit_2_1360.text()))
    else:
        self.stats.balance[1360].append(0)
    if self.lineEdit_2_1370.text():
        self.stats.balance[1370].append(int(self.lineEdit_2_1370.text()))
    else:
        self.stats.balance[1370].append(0)
    if self.lineEdit_2_1300.text():
        self.stats.balance[1300].append(int(self.lineEdit_2_1300.text()))
    else:
        self.stats.balance[1300].append(0)
    if self.lineEdit_2_1410.text():
        self.stats.balance[1410].append(int(self.lineEdit_2_1410.text()))
    else:
        self.stats.balance[1410].append(0)
    if self.lineEdit_2_1420.text():
        self.stats.balance[1420].append(int(self.lineEdit_2_1420.text()))
    else:
        self.stats.balance[1420].append(0)
    if self.lineEdit_2_1430.text():
        self.stats.balance[1430].append(int(self.lineEdit_2_1430.text()))
    else:
        self.stats.balance[1430].append(0)
    if self.lineEdit_2_1450.text():
        self.stats.balance[1450].append(int(self.lineEdit_2_1450.text()))
    else:
        self.stats.balance[1450].append(0)
    if self.lineEdit_2_1400.text():
        self.stats.balance[1400].append(int(self.lineEdit_2_1400.text()))
    else:
        self.stats.balance[1400].append(0)
    if self.lineEdit_2_1510.text():
        self.stats.balance[1510].append(int(self.lineEdit_2_1510.text()))
    else:
        self.stats.balance[1510].append(0)
    if self.lineEdit_2_1520.text():
        self.stats.balance[1520].append(int(self.lineEdit_2_1520.text()))
    else:
        self.stats.balance[1520].append(0)
    if self.lineEdit_2_1530.text():
        self.stats.balance[1530].append(int(self.lineEdit_2_1530.text()))
    else:
        self.stats.balance[1530].append(0)
    if self.lineEdit_2_1540.text():
        self.stats.balance[1540].append(int(self.lineEdit_2_1540.text()))
    else:
        self.stats.balance[1540].append(0)
    if self.lineEdit_2_1550.text():
        self.stats.balance[1550].append(int(self.lineEdit_2_1550.text()))
    else:
        self.stats.balance[1550].append(0)
    if self.lineEdit_2_1500.text():
        self.stats.balance[1500].append(int(self.lineEdit_2_1500.text()))
    else:
        self.stats.balance[1500].append(0)
    if self.lineEdit_2_1700.text():
        self.stats.balance[1700].append(int(self.lineEdit_2_1700.text()))
    else:
        self.stats.balance[1700].append(0)
    #3
    if self.lineEdit_3_1110.text():
        self.stats.balance[1110].append(int(self.lineEdit_3_1110.text()))
    else:
        self.stats.balance[1110].append(0)
    if self.lineEdit_3_1120.text():
        self.stats.balance[1120].append(int(self.lineEdit_3_1120.text()))
    else:
        self.stats.balance[1120].append(0)
    if self.lineEdit_3_1130.text():
        self.stats.balance[1130].append(int(self.lineEdit_3_1130.text()))
    else:
        self.stats.balance[1130].append(0)
    if self.lineEdit_3_1140.text():
        self.stats.balance[1140].append(int(self.lineEdit_3_1140.text()))
    else:
        self.stats.balance[1140].append(0)
    if self.lineEdit_3_1150.text():
        self.stats.balance[1150].append(int(self.lineEdit_3_1150.text()))
    else:
        self.stats.balance[1150].append(0)
    if self.lineEdit_3_1160.text():
        self.stats.balance[1160].append(int(self.lineEdit_3_1160.text()))
    else:
        self.stats.balance[1160].append(0)
    if self.lineEdit_3_1170.text():
        self.stats.balance[1170].append(int(self.lineEdit_3_1170.text()))
    else:
        self.stats.balance[1170].append(0)
    if self.lineEdit_3_1180.text():
        self.stats.balance[1180].append(int(self.lineEdit_3_1180.text()))
    else:
        self.stats.balance[1180].append(0)
    if self.lineEdit_3_1190.text():
        self.stats.balance[1190].append(int(self.lineEdit_3_1190.text()))
    else:
        self.stats.balance[1190].append(0)
    if self.lineEdit_3_1100.text():
        self.stats.balance[1100].append(int(self.lineEdit_3_1100.text()))
    else:
        self.stats.balance[1100].append(0)
    if self.lineEdit_3_1210.text():
        self.stats.balance[1210].append(int(self.lineEdit_3_1210.text()))
    else:
        self.stats.balance[1210].append(0)
    if self.lineEdit_3_1220.text():
        self.stats.balance[1220].append(int(self.lineEdit_3_1220.text()))
    else:
        self.stats.balance[1220].append(0)
    if self.lineEdit_3_1230.text():
        self.stats.balance[1230].append(int(self.lineEdit_3_1230.text()))
    else:
        self.stats.balance[1230].append(0)
    if self.lineEdit_3_1240.text():
        self.stats.balance[1240].append(int(self.lineEdit_3_1240.text()))
    else:
        self.stats.balance[1240].append(0)
    if self.lineEdit_3_1250.text():
        self.stats.balance[1250].append(int(self.lineEdit_3_1250.text()))
    else:
        self.stats.balance[1250].append(0)
    if self.lineEdit_3_1260.text():
        self.stats.balance[1260].append(int(self.lineEdit_3_1260.text()))
    else:
        self.stats.balance[1260].append(0)
    if self.lineEdit_3_1200.text():
        self.stats.balance[1200].append(int(self.lineEdit_3_1200.text()))
    else:
        self.stats.balance[1200].append(0)
    if self.lineEdit_3_1600.text():
        self.stats.balance[1600].append(int(self.lineEdit_3_1600.text()))
    else:
        self.stats.balance[1600].append(0)
    # пассив
    if self.lineEdit_3_1310.text():
        self.stats.balance[1310].append(int(self.lineEdit_3_1310.text()))
    else:
        self.stats.balance[1310].append(0)
    if self.lineEdit_3_1320.text():
        self.stats.balance[1320].append(int(self.lineEdit_3_1320.text()))
    else:
        self.stats.balance[1320].append(0)
    if self.lineEdit_3_1340.text():
        self.stats.balance[1340].append(int(self.lineEdit_3_1340.text()))
    else:
        self.stats.balance[1340].append(0)
    if self.lineEdit_3_1350.text():
        self.stats.balance[1350].append(int(self.lineEdit_3_1350.text()))
    else:
        self.stats.balance[1350].append(0)
    if self.lineEdit_3_1360.text():
        self.stats.balance[1360].append(int(self.lineEdit_3_1360.text()))
    else:
        self.stats.balance[1360].append(0)
    if self.lineEdit_3_1370.text():
        self.stats.balance[1370].append(int(self.lineEdit_3_1370.text()))
    else:
        self.stats.balance[1370].append(0)
    if self.lineEdit_3_1300.text():
        self.stats.balance[1300].append(int(self.lineEdit_3_1300.text()))
    else:
        self.stats.balance[1300].append(0)
    if self.lineEdit_3_1410.text():
        self.stats.balance[1410].append(int(self.lineEdit_3_1410.text()))
    else:
        self.stats.balance[1410].append(0)
    if self.lineEdit_3_1420.text():
        self.stats.balance[1420].append(int(self.lineEdit_3_1420.text()))
    else:
        self.stats.balance[1420].append(0)
    if self.lineEdit_3_1430.text():
        self.stats.balance[1430].append(int(self.lineEdit_3_1430.text()))
    else:
        self.stats.balance[1430].append(0)
    if self.lineEdit_3_1450.text():
        self.stats.balance[1450].append(int(self.lineEdit_3_1450.text()))
    else:
        self.stats.balance[1450].append(0)
    if self.lineEdit_3_1400.text():
        self.stats.balance[1400].append(int(self.lineEdit_3_1400.text()))
    else:
        self.stats.balance[1400].append(0)
    if self.lineEdit_3_1510.text():
        self.stats.balance[1510].append(int(self.lineEdit_3_1510.text()))
    else:
        self.stats.balance[1510].append(0)
    if self.lineEdit_3_1520.text():
        self.stats.balance[1520].append(int(self.lineEdit_3_1520.text()))
    else:
        self.stats.balance[1520].append(0)
    if self.lineEdit_3_1530.text():
        self.stats.balance[1530].append(int(self.lineEdit_3_1530.text()))
    else:
        self.stats.balance[1530].append(0)
    if self.lineEdit_3_1540.text():
        self.stats.balance[1540].append(int(self.lineEdit_3_1540.text()))
    else:
        self.stats.balance[1540].append(0)
    if self.lineEdit_3_1550.text():
        self.stats.balance[1550].append(int(self.lineEdit_3_1550.text()))
    else:
        self.stats.balance[1550].append(0)
    if self.lineEdit_3_1500.text():
        self.stats.balance[1500].append(int(self.lineEdit_3_1500.text()))
    else:
        self.stats.balance[1500].append(0)
    if self.lineEdit_3_1700.text():
        self.stats.balance[1700].append(int(self.lineEdit_3_1700.text()))
    else:
        self.stats.balance[1700].append(0)
    for i in self.stats.balance:
        print(i, self.stats.balance[i])
    print()
    #ofr
    #0
    if self.lineEdit_0_2110.text():
        self.stats.ofr[2110] = [int(self.lineEdit_0_2110.text())]
    else:
        self.stats.ofr[2110] = [0]
    if self.lineEdit_0_2120.text():
        self.stats.ofr[2120] = [int(self.lineEdit_0_2120.text())]
    else:
        self.stats.ofr[2120] = [0]
    if self.lineEdit_0_2100.text():
        self.stats.ofr[2100] = [int(self.lineEdit_0_2100.text())]
    else:
        self.stats.ofr[2100] = [0]
    if self.lineEdit_0_2210.text():
        self.stats.ofr[2210] = [int(self.lineEdit_0_2210.text())]
    else:
        self.stats.ofr[2210] = [0]
    if self.lineEdit_0_2220.text():
        self.stats.ofr[2220] = [int(self.lineEdit_0_2220.text())]
    else:
        self.stats.ofr[2220] = [0]
    if self.lineEdit_0_2200.text():
        self.stats.ofr[2200] = [int(self.lineEdit_0_2200.text())]
    else:
        self.stats.ofr[2200] = [0]
    if self.lineEdit_0_2310.text():
        self.stats.ofr[2310] = [int(self.lineEdit_0_2310.text())]
    else:
        self.stats.ofr[2310] = [0]
    if self.lineEdit_0_2320.text():
        self.stats.ofr[2320] = [int(self.lineEdit_0_2320.text())]
    else:
        self.stats.ofr[2320] = [0]
    if self.lineEdit_0_2330.text():
        self.stats.ofr[2330] = [int(self.lineEdit_0_2330.text())]
    else:
        self.stats.ofr[2330] = [0]
    if self.lineEdit_0_2340.text():
        self.stats.ofr[2340] = [int(self.lineEdit_0_2340.text())]
    else:
        self.stats.ofr[2340] = [0]
    if self.lineEdit_0_2350.text():
        self.stats.ofr[2350] = [int(self.lineEdit_0_2350.text())]
    else:
        self.stats.ofr[2350] = [0]
    if self.lineEdit_0_2300.text():
        self.stats.ofr[2300] = [int(self.lineEdit_0_2300.text())]
    else:
        self.stats.ofr[2300] = [0]
    if self.lineEdit_0_2410.text():
        self.stats.ofr[2410] = [int(self.lineEdit_0_2410.text())]
    else:
        self.stats.ofr[2410] = [0]
    if self.lineEdit_0_2421.text():
        self.stats.ofr[2421] = [int(self.lineEdit_0_2421.text())]
    else:
        self.stats.ofr[2421] = [0]
    if self.lineEdit_0_2430.text():
        self.stats.ofr[2430] = [int(self.lineEdit_0_2430.text())]
    else:
        self.stats.ofr[2430] = [0]
    if self.lineEdit_0_2450.text():
        self.stats.ofr[2450] = [int(self.lineEdit_0_2450.text())]
    else:
        self.stats.ofr[2450] = [0]
    if self.lineEdit_0_2460.text():
        self.stats.ofr[2460] = [int(self.lineEdit_0_2460.text())]
    else:
        self.stats.ofr[2460] = [0]
    if self.lineEdit_0_2400.text():
        self.stats.ofr[2400] = [int(self.lineEdit_0_2400.text())]
    else:
        self.stats.ofr[2400] = [0]
    #1
    if self.lineEdit_1_2110.text():
        self.stats.ofr[2110].append(int(self.lineEdit_1_2110.text()))
    else:
        self.stats.ofr[2110].append(0)
    if self.lineEdit_1_2120.text():
        self.stats.ofr[2120].append(int(self.lineEdit_1_2120.text()))
    else:
        self.stats.ofr[2120].append(0)
    if self.lineEdit_1_2100.text():
        self.stats.ofr[2100].append(int(self.lineEdit_1_2100.text()))
    else:
        self.stats.ofr[2100].append(0)
    if self.lineEdit_1_2210.text():
        self.stats.ofr[2210].append(int(self.lineEdit_1_2210.text()))
    else:
        self.stats.ofr[2210].append(0)
    if self.lineEdit_1_2220.text():
        self.stats.ofr[2220].append(int(self.lineEdit_1_2220.text()))
    else:
        self.stats.ofr[2220].append(0)
    if self.lineEdit_1_2200.text():
        self.stats.ofr[2200].append(int(self.lineEdit_1_2200.text()))
    else:
        self.stats.ofr[2200].append(0)
    if self.lineEdit_1_2310.text():
        self.stats.ofr[2310].append(int(self.lineEdit_1_2310.text()))
    else:
        self.stats.ofr[2310].append(0)
    if self.lineEdit_1_2320.text():
        self.stats.ofr[2320].append(int(self.lineEdit_1_2320.text()))
    else:
        self.stats.ofr[2320].append(0)
    if self.lineEdit_1_2330.text():
        self.stats.ofr[2330].append(int(self.lineEdit_1_2330.text()))
    else:
        self.stats.ofr[2330].append(0)
    if self.lineEdit_1_2340.text():
        self.stats.ofr[2340].append(int(self.lineEdit_1_2340.text()))
    else:
        self.stats.ofr[2340].append(0)
    if self.lineEdit_1_2350.text():
        self.stats.ofr[2350].append(int(self.lineEdit_1_2350.text()))
    else:
        self.stats.ofr[2350].append(0)
    if self.lineEdit_1_2300.text():
        self.stats.ofr[2300].append(int(self.lineEdit_1_2300.text()))
    else:
        self.stats.ofr[2300].append(0)
    if self.lineEdit_1_2410.text():
        self.stats.ofr[2410].append(int(self.lineEdit_1_2410.text()))
    else:
        self.stats.ofr[2410].append(0)
    if self.lineEdit_1_2421.text():
        self.stats.ofr[2421].append(int(self.lineEdit_1_2421.text()))
    else:
        self.stats.ofr[2421].append(0)
    if self.lineEdit_1_2430.text():
        self.stats.ofr[2430].append(int(self.lineEdit_1_2430.text()))
    else:
        self.stats.ofr[2430].append(0)
    if self.lineEdit_1_2450.text():
        self.stats.ofr[2450].append(int(self.lineEdit_1_2450.text()))
    else:
        self.stats.ofr[2450].append(0)
    if self.lineEdit_1_2460.text():
        self.stats.ofr[2460].append(int(self.lineEdit_1_2460.text()))
    else:
        self.stats.ofr[2460].append(0)
    if self.lineEdit_1_2400.text():
        self.stats.ofr[2400].append(int(self.lineEdit_1_2400.text()))
    else:
        self.stats.ofr[2400].append(0)
    # 2
    if self.lineEdit_2_2110.text():
        self.stats.ofr[2110].append(int(self.lineEdit_2_2110.text()))
    else:
        self.stats.ofr[2110].append(0)
    if self.lineEdit_2_2120.text():
        self.stats.ofr[2120].append(int(self.lineEdit_2_2120.text()))
    else:
        self.stats.ofr[2120].append(0)
    if self.lineEdit_2_2100.text():
        self.stats.ofr[2100].append(int(self.lineEdit_2_2100.text()))
    else:
        self.stats.ofr[2100].append(0)
    if self.lineEdit_2_2210.text():
        self.stats.ofr[2210].append(int(self.lineEdit_2_2210.text()))
    else:
        self.stats.ofr[2210].append(0)
    if self.lineEdit_2_2220.text():
        self.stats.ofr[2220].append(int(self.lineEdit_2_2220.text()))
    else:
        self.stats.ofr[2220].append(0)
    if self.lineEdit_2_2200.text():
        self.stats.ofr[2200].append(int(self.lineEdit_2_2200.text()))
    else:
        self.stats.ofr[2200].append(0)
    if self.lineEdit_2_2310.text():
        self.stats.ofr[2310].append(int(self.lineEdit_2_2310.text()))
    else:
        self.stats.ofr[2310].append(0)
    if self.lineEdit_2_2320.text():
        self.stats.ofr[2320].append(int(self.lineEdit_2_2320.text()))
    else:
        self.stats.ofr[2320].append(0)
    if self.lineEdit_2_2330.text():
        self.stats.ofr[2330].append(int(self.lineEdit_2_2330.text()))
    else:
        self.stats.ofr[2330].append(0)
    if self.lineEdit_2_2340.text():
        self.stats.ofr[2340].append(int(self.lineEdit_2_2340.text()))
    else:
        self.stats.ofr[2340].append(0)
    if self.lineEdit_2_2350.text():
        self.stats.ofr[2350].append(int(self.lineEdit_2_2350.text()))
    else:
        self.stats.ofr[2350].append(0)
    if self.lineEdit_2_2300.text():
        self.stats.ofr[2300].append(int(self.lineEdit_2_2300.text()))
    else:
        self.stats.ofr[2300].append(0)
    if self.lineEdit_2_2410.text():
        self.stats.ofr[2410].append(int(self.lineEdit_2_2410.text()))
    else:
        self.stats.ofr[2410].append(0)
    if self.lineEdit_2_2421.text():
        self.stats.ofr[2421].append(int(self.lineEdit_2_2421.text()))
    else:
        self.stats.ofr[2421].append(0)
    if self.lineEdit_2_2430.text():
        self.stats.ofr[2430].append(int(self.lineEdit_2_2430.text()))
    else:
        self.stats.ofr[2430].append(0)
    if self.lineEdit_2_2450.text():
        self.stats.ofr[2450].append(int(self.lineEdit_2_2450.text()))
    else:
        self.stats.ofr[2450].append(0)
    if self.lineEdit_2_2460.text():
        self.stats.ofr[2460].append(int(self.lineEdit_2_2460.text()))
    else:
        self.stats.ofr[2460].append(0)
    if self.lineEdit_2_2400.text():
        self.stats.ofr[2400].append(int(self.lineEdit_2_2400.text()))
    else:
        self.stats.ofr[2400].append(0)
    # 3
    if self.lineEdit_3_2110.text():
        self.stats.ofr[2110].append(int(self.lineEdit_3_2110.text()))
    else:
        self.stats.ofr[2110].append(0)
    if self.lineEdit_3_2120.text():
        self.stats.ofr[2120].append(int(self.lineEdit_3_2120.text()))
    else:
        self.stats.ofr[2120].append(0)
    if self.lineEdit_3_2100.text():
        self.stats.ofr[2100].append(int(self.lineEdit_3_2100.text()))
    else:
        self.stats.ofr[2100].append(0)
    if self.lineEdit_3_2210.text():
        self.stats.ofr[2210].append(int(self.lineEdit_3_2210.text()))
    else:
        self.stats.ofr[2210].append(0)
    if self.lineEdit_3_2220.text():
        self.stats.ofr[2220].append(int(self.lineEdit_3_2220.text()))
    else:
        self.stats.ofr[2220].append(0)
    if self.lineEdit_3_2200.text():
        self.stats.ofr[2200].append(int(self.lineEdit_3_2200.text()))
    else:
        self.stats.ofr[2200].append(0)
    if self.lineEdit_3_2310.text():
        self.stats.ofr[2310].append(int(self.lineEdit_3_2310.text()))
    else:
        self.stats.ofr[2310].append(0)
    if self.lineEdit_3_2320.text():
        self.stats.ofr[2320].append(int(self.lineEdit_3_2320.text()))
    else:
        self.stats.ofr[2320].append(0)
    if self.lineEdit_3_2330.text():
        self.stats.ofr[2330].append(int(self.lineEdit_3_2330.text()))
    else:
        self.stats.ofr[2330].append(0)
    if self.lineEdit_3_2340.text():
        self.stats.ofr[2340].append(int(self.lineEdit_3_2340.text()))
    else:
        self.stats.ofr[2340].append(0)
    if self.lineEdit_3_2350.text():
        self.stats.ofr[2350].append(int(self.lineEdit_3_2350.text()))
    else:
        self.stats.ofr[2350].append(0)
    if self.lineEdit_3_2300.text():
        self.stats.ofr[2300].append(int(self.lineEdit_3_2300.text()))
    else:
        self.stats.ofr[2300].append(0)
    if self.lineEdit_3_2410.text():
        self.stats.ofr[2410].append(int(self.lineEdit_3_2410.text()))
    else:
        self.stats.ofr[2410].append(0)
    if self.lineEdit_3_2421.text():
        self.stats.ofr[2421].append(int(self.lineEdit_3_2421.text()))
    else:
        self.stats.ofr[2421].append(0)
    if self.lineEdit_3_2430.text():
        self.stats.ofr[2430].append(int(self.lineEdit_3_2430.text()))
    else:
        self.stats.ofr[2430].append(0)
    if self.lineEdit_3_2450.text():
        self.stats.ofr[2450].append(int(self.lineEdit_3_2450.text()))
    else:
        self.stats.ofr[2450].append(0)
    if self.lineEdit_3_2460.text():
        self.stats.ofr[2460].append(int(self.lineEdit_3_2460.text()))
    else:
        self.stats.ofr[2460].append(0)
    if self.lineEdit_3_2400.text():
        self.stats.ofr[2400].append(int(self.lineEdit_3_2400.text()))
    else:
        self.stats.ofr[2400].append(0)
    for i in self.stats.ofr:
        print(i, self.stats.ofr[i])
    print()