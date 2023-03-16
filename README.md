# Financial Analysis Tool for Windows
Десктопное приложение для финансового анализа компании на основе ее отчетности c расчетом и визуализацией коэффициентов. 

Приложение для финансового анализа позволяет пользователям визуализировать и анализировать финансовую отчетность в формате РСБУ (Российский стандарт бухгалтерского учета). Приложение разработано с помощью Python на основе библиотеки PyQt 5 и нескольких других вспомогательных библиотек (pandas, numpy и др.). Дизайн графического интерфейса выполнен в Qt Designer.

Пользователи могут просматривать бухгалтерский баланс с его активом и пассивом, отчет о финансовых результатах и другие финансовые формы. Пользователь может использовать слайдеры для корректировки значений в строках статей или переключиться в режим ручного ввода данных. Кнопка «Случайные значения» генерирует набор случайных данных для всех форм отчетности на основе специально разработанного алгоритма, учитывающего распределение весов строк в статьях. Также, благодаря алгоритму соблюдаются принципы бухгалтерского учета - каждый раздел суммируется в валюту баланса, а актив и пассив равны друг другу.

![alt text](https://github.com/DmitryKostin/financial-analysis-visualizer/blob/main/promo_1.jpg?raw=true)

После ввода данных финансовой отчетности пользователь может нажать кнопку «Go» для рассчета коэффициентов финансового анализа, которые отобразятся в отдельном окне. Значения коэффициентов выделены зеленым и красным цветом в зависимости от того, соответствуют ли они рекомендуемым критериям. Приложение также позволяет пользователям визуализировать процесс расчета метрик, расписывая все необходимые арифметические действия шаг за шагом. Во втором окне есть несколько вкладок, где пользователь может просматривать расчеты каждого из коэффициента во всех нужных периодах, а также строить интерактивные графики для дальнейшего анализа данных.

![alt text](https://github.com/DmitryKostin/financial-analysis-visualizer/blob/main/promo_2.jpg?raw=true)

text

![alt text](https://github.com/DmitryKostin/financial-analysis-visualizer/blob/main/promo_3.jpg?raw=true)

Этот инструмент в первую очередь предназначен для пользователей, изучающих финансовый анализ и бухгалтерский учет. Приложение могло бы быть полезным для тех, кто хочет изучить взаимосвязь между различными финансовыми показателями и посмотреть, как они влияют друг на друга. Приложение также может быть полезно иностранным студентам, которые хотят изучать российский стандарт отчетности или только знакомятся с ним. Хотя инструмент в первую очередь предназначен для российских пользователей, он также может быть адаптирован к другим мировым стандартам бухгалтерского учета.

Надеюсь, это приложение станет полезным ресурсом для финансовых аналитиков, бухгалтеров и студентов, изучающих финансовый анализ и бухгалтерский учет.
