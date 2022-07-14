
FL_PM_PAGES = 'https://www.lotteryusa.com/'
FL_PM_PICK2 = "https://www.lotteryusa.com/florida/pick-2/"
FL_PM_PICK3 = 'https://www.lotteryusa.com/florida/pick-3/'
FL_PM_PICK4 = 'https://www.lotteryusa.com/florida/pick-4/'

FL_P2_fecha = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time'
FL_P2_NU1 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[1]/span'
FL_P2_NU2 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span'

FL_P3_fecha = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time'
FL_P3_NU1 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[1]/span'
FL_P3_NU2 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span'
FL_P3_NU3 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span'

FL_P4_fecha ='/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time'
FL_P4_NU1 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[1]/span'
FL_P4_NU2 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span'
FL_P4_NU3 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span'
FL_P4_NU4 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[4]/span'

FLORIDA_LOTTERY_USA_PM = {
    'URL'     : [FL_PM_PAGES,FL_PM_PICK3,FL_PM_PICK4],
    "PICK3"    : [FL_P3_fecha,FL_P3_NU1,FL_P3_NU2,FL_P3_NU3 ],
    "PICK4"  : [FL_P4_fecha,FL_P4_NU1,FL_P4_NU2,FL_P4_NU3,FL_P4_NU4]
}

FLORIDA_PM_TODO = [FLORIDA_LOTTERY_USA_PM ]