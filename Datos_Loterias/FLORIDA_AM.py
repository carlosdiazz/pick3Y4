
#! ---------------------------------------------------------------------------------------------------------------------------------
FL_AM_PAGES = 'https://www.lotteryusa.com/'
FL_AM_PICK3 = 'https://www.lotteryusa.com/florida/midday-pick-3/'
FL_AM_PICK4 = 'https://www.lotteryusa.com/florida/midday-pick-4/'

FL_P3_FECHA = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time'
FL_P3_NU1 = "/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[1]/span"
FL_P3_NU2 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span'
FL_P3_NU3 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span'

FL_P4_FECHA ='/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time'
FL_P4_NU1 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[1]/span'
FL_P4_NU2 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span'
FL_P4_NU3 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span'
FL_P4_NU4 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[4]/span'

FLORIDA_LOTTERY_USA_AM = {
    'URL'       : [FL_AM_PAGES,FL_AM_PICK3,FL_AM_PICK4],
    "PICK3"     : [FL_P3_FECHA,FL_P3_NU1,FL_P3_NU2,FL_P3_NU3],
    "PICK4"     : [FL_P4_FECHA,FL_P4_NU1,FL_P4_NU2,FL_P4_NU3,FL_P4_NU4 ]
}

#! ----------------------------------------------------------------------------------------------------------------------------------

FLORIDA_AM_TODO = [FLORIDA_LOTTERY_USA_AM ]