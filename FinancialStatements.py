class FinancialStatements:
    def __init__(self):
        self.balance = {
            1110: [],
            1120: [],
            1130: []
        }
        self.ofr = {
            2100: [],
            2200: [],
        }
        self.indicators = {
            'Коэффициент текущей ликвидности': [],
            'Коэффициент быстрой ликвидности': [],
            'Коэффициент абсолютной ликвидности': [],
            'Коэффициент финансовой независимости': [],
            'Коэффициент финансового рычага': [],
            'Коэффициент обеспеченности собственными оборотными средствами': [],
            'Коэффициент оборачиваемости запасов': [],
            'Период оборота запасов': [],
            'Коэффициент оборачиваемости дебиторской задолженности': [],
            'Период оборота дебиторской задолженности': [],
            'Коэффициент оборачиваемости кредиторской задолженности': [],
            'Период оборота кредиторской задолженности': [],
            'Операционный цикл': [],
            'Финансовый цикл': [],
            'Рентабельность активов': [],
            'Рентабельность собственного капитала': [],
            'Рентабельность прибыли от продаж': [],
            'Маржа чистой прибыли': []
        }

    def current_liquidity(self, period=0, digits=2):
        #1,0-2,0
        try:
            k = self.balance[1200][period] / (self.balance[1510][period] + self.balance[1520][period] + self.balance[1550][period])
            self.indicators['Коэффициент текущей ликвидности'].append(round(k, digits))
            return round(k, digits)
        except ZeroDivisionError:
            self.indicators['Коэффициент текущей ликвидности'].append('n/a')
            return 0

    def fast_liquidity(self, period=0, digits=2):
        try:
            k = (self.balance[1230][period] +
                 self.balance[1240][period] +
                 self.balance[1250][period]) / \
                (self.balance[1510][period] +
                 self.balance[1520][period] +
                 self.balance[1540][period] +
                 self.balance[1550][period])
            self.indicators['Коэффициент быстрой ликвидности'].append(round(k, digits))
            return round(k, digits)
        except ZeroDivisionError:
            self.indicators['Коэффициент быстрой ликвидности'].append('n/a')
            return 0

    def absolute_liquidity(self, period=0, digits=2):
        try:
            k = (self.balance[1240][period] +
                 self.balance[1250][period]) / \
                (self.balance[1510][period] +
                 self.balance[1520][period] +
                 self.balance[1550][period])
            self.indicators['Коэффициент абсолютной ликвидности'].append(round(k, digits))
            return round(k, digits)
        except ZeroDivisionError:
            self.indicators['Коэффициент абсолютной ликвидности'].append('n/a')
            return 0

    def financial_independence(self, period=0, digits=2):
        try:
            k = self.balance[1300][period] / self.balance[1700][period]
            self.indicators['Коэффициент финансовой независимости'].append(round(k, digits))
            return round(k, digits)
        except ZeroDivisionError:
            self.indicators['Коэффициент финансовой независимости'].append('n/a')
            return 0

    def leverage_ratio(self, period=0, digits=2):
        #1410 + 1510 / 1300
        try:
            k = (self.balance[1410][period] + self.balance[1510][period]) / self.balance[1300][period]
            self.indicators['Коэффициент финансового рычага'].append(round(k, digits))
            return round(k, digits)
        except ZeroDivisionError:
            self.indicators['Коэффициент финансового рычага'].append('n/a')
            return 0

    def own_working_capital(self, period=0, digits=2):
        #Коэффициент обеспеченности собственными оборотными средствами
        try:
            k = (self.balance[1300][period] -
                 self.balance[1100][period]) / \
                self.balance[1200][period]
            self.indicators['Коэффициент обеспеченности собственными оборотными средствами'].append(round(k, digits))
            return round(k, digits)
        except ZeroDivisionError:
            self.indicators['Коэффициент обеспеченности собственными оборотными средствами'].append('n/a')
            return 0

    def inventory_turnover_ratio(self, period=0, digits=2):
        #коэффициент оборачиваемости запасов
        try:
            k = (self.ofr[2120][period] +
                 self.ofr[2210][period] +
                 self.ofr[2220][period]) / \
                (self.balance[1210][period] +
                 self.balance[1220][period])
            self.indicators['Коэффициент оборачиваемости запасов'].append(round(k, digits))
            return round(k, digits)
        except ZeroDivisionError:
            self.indicators['Коэффициент оборачиваемости запасов'].append('n/a')
            return 0

    def inventory_turnover_period(self, period=0):
        #Период оборота запасов
        try:
            k = 365 / self.inventory_turnover_ratio(period)
            self.indicators['Период оборота запасов'].append(ceil(k))
            return ceil(k)
        except ZeroDivisionError:
            self.indicators['Период оборота запасов'].append('n/a')
            return 0

    def accounts_receivable_turnover_ratio(self, period=0, digits=2):
        #коэффициент оборачиваемости дебиторской задолженности
        try:
            k = (self.ofr[2110][period] / self.balance[1230][period])
            self.indicators['Коэффициент оборачиваемости дебиторской задолженности'].append(round(k, digits))
            return round(k, digits)
        except ZeroDivisionError:
            self.indicators['Коэффициент оборачиваемости дебиторской задолженности'].append('n/a')
            return 0

    def accounts_receivable_turnover_period(self, period=0):
        #Период оборота дебиторской задолженности
        try:
            k = 365 / self.accounts_receivable_turnover_ratio(period)
            self.indicators['Период оборота дебиторской задолженности'].append(ceil(k))
            return ceil(k)
        except ZeroDivisionError:
            self.indicators['Период оборота дебиторской задолженности'].append('n/a')
            return 0

    def accounts_payable_turnover_ratio(self, period=0, digits=2):
        #коэффициент оборачиваемости кредиторской задолженности
        try:
            k = (self.ofr[2120][period] / self.balance[1520][period])
            self.indicators['Коэффициент оборачиваемости кредиторской задолженности'].append(round(k, digits))
            return round(k, digits)
        except ZeroDivisionError:
            self.indicators['Коэффициент оборачиваемости кредиторской задолженности'].append('n/a')
            return 0

    def accounts_payable_turnover_period(self, period=0):
        #период оборота кредиторской задолженности
        try:
            k = 365 / self.accounts_payable_turnover_ratio(period)
            self.indicators['Период оборота кредиторской задолженности'].append(ceil(k))
            return ceil(k)
        except ZeroDivisionError:
            self.indicators['Период оборота кредиторской задолженности'].append('n/a')
            return 0

    def operating_cycle(self, period=0):
        #операционный цикл
        k = self.inventory_turnover_period(period) + self.accounts_receivable_turnover_period(period)
        self.indicators['Операционный цикл'].append(ceil(k))
        return ceil(k)

    def financial_cycle(self, period=0):
        k = self.operating_cycle(period) - self.accounts_payable_turnover_period(period)
        self.indicators['Финансовый цикл'].append(ceil(k))
        return ceil(k)

    def return_on_assets(self, period=0, digits=2):
        #рентабельность активов ROA
        try:
            k = self.ofr[2400][period] / self.balance[1600][period]
            self.indicators['Рентабельность активов'].append(round(k, digits))
            return round(k, digits)
        except ZeroDivisionError:
            self.indicators['Рентабельность активов'].append('n/a')
            return 0

    def return_on_equity(self, period=0, digits=2):
        #рентабельность собственного капитала ROE
        try:
            k = self.ofr[2400][period] / self.balance[1300][period]
            self.indicators['Рентабельность собственного капитала'].append(round(k, digits))
            return round(k, digits)
        except ZeroDivisionError:
            self.indicators['Рентабельность собственного капитала'].append('n/a')
            return 0

    def return_on_profit_from_sales(self, period=0, digits=2):
        #Рентабельность прибыли от продаж
        try:
            k = self.ofr[2200][period] / self.ofr[2110][period]
            self.indicators['Рентабельность прибыли от продаж'].append(round(k, digits))
            return round(k, digits)
        except ZeroDivisionError:
            self.indicators['Рентабельность прибыли от продаж'].append('n/a')
            return 0

    def net_profit_margin(self, period=0, digits=2):
        #маржа чистой прибыли
        try:
            k = self.ofr[2400][period] / self.ofr[2110][period]
            self.indicators['Маржа чистой прибыли'].append(round(k, digits))
            return round(k, digits)
        except ZeroDivisionError:
            self.indicators['Маржа чистой прибыли'].append('n/a')
            return 0

    # Визуализация
    def vis_cur_liq(self, period=0):
        s = str(f'{self.balance[1200][period]} / ({self.balance[1510][period]} + {self.balance[1520][period]} + {self.balance[1550][period]}) = {self.current_liquidity(period)}')
        print(s)
        return s

    def vis_fast_liq(self, period=0):
        s = str(f'({self.balance[1230][period]} + {self.balance[1240][period]} + {self.balance[1250][period]})/({self.balance[1510][period] + self.balance[1520][period]} + {self.balance[1540][period] + self.balance[1550][period]}) = {self.fast_liquidity(period)}')
        print(s)
        return s

    def vis_abs_liq(self, period=0):
        s = str(f'({self.balance[1240][period]} + {self.balance[1250][period]}) / ({self.balance[1510][period]} + {self.balance[1520][period]} + {self.balance[1550][period]}) = {self.absolute_liquidity(period)}')
        print(s)
        return s

    def vis_fin_ind(self, period=0):
        s = str(f'{self.balance[1300][period]} / {self.balance[1700][period]} = {self.financial_independence(period)}')
        print(s)
        return s

    def vis_lev_rat(self, period=0):
        s = str(f'({self.balance[1410][period]} + {self.balance[1510][period]}) / {self.balance[1300][period]} = {self.leverage_ratio(period)}')
        print(s)
        return s

    def vis_work_cap(self, period=0):
        s = str(f'({self.balance[1300][period]} - {self.balance[1100][period]}) / {self.balance[1200][period]} = {self.own_working_capital(period)}')
        print(s)
        return s

    def vis_inv_rat(self, period=0):
        s = str(f'({self.ofr[2120][period]} + {self.ofr[2210][period]} + {self.ofr[2220][period]}) / ({self.balance[1210][period]} + {self.balance[1220][period]}) = {self.inventory_turnover_ratio(period)}')
        print(s)
        return s

    def vis_inv_per(self, period=0):
        s = str(f'365 / {self.inventory_turnover_ratio(period)} = {self.inventory_turnover_period(period)}')
        print(s)
        return s

    def vis_rec_rat(self, period=0):
        s = str(f'({self.ofr[2110][period]} / {self.balance[1230][period]}) = {self.accounts_receivable_turnover_ratio(period)}')
        print(s)
        return s

    def vis_rec_per(self, period=0):
        s = str(f'365 / {self.accounts_receivable_turnover_ratio(period)} = {self.accounts_receivable_turnover_period(period)}')
        print(s)
        return s

    def vis_pay_rat(self, period=0):
        s = str(f'({self.ofr[2120][period]} / {self.balance[1520][period]}) = {self.accounts_payable_turnover_ratio(period)}')
        print(s)
        return s

    def vis_pay_per(self, period=0):
        s = str(f'365 / {self.accounts_payable_turnover_ratio(period)} = {self.accounts_payable_turnover_period(period)}')
        print(s)
        return s

    def vis_oper_cyc(self, period=0):
        s = str(f'{self.inventory_turnover_period(period)} + {self.accounts_receivable_turnover_period(period)} = {self.operating_cycle(period)}')
        print(s)
        return s

    def vis_fin_cyc(self, period=0):
        s = str(f'{self.operating_cycle(period)} - {self.accounts_payable_turnover_period(period)} = {self.financial_cycle(period)}')
        print(s)
        return s

    def vis_roa(self, period=0):
        s = str(f'{self.ofr[2400][period]} / {self.balance[1600][period]} = {self.return_on_assets(period)}')
        print(s)
        return s

    def vis_roe(self, period=0):
        s = str(f'{self.ofr[2400][period]} / {self.balance[1300][period]} = {self.return_on_equity(period)}')
        print(s)
        return s

    def vis_ropfs(self, period=0):
        s = str(f'{self.ofr[2200][period]} / {self.ofr[2110][period]} = {self.return_on_profit_from_sales(period)}')
        print(s)
        return s

    def vis_net_mar(self, period=0):
        s = str(f'{self.ofr[2400][period]} / {self.ofr[2110][period]} = {self.net_profit_margin(period)}')
        print(s)
        return s