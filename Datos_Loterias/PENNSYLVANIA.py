
#! ---------------------------------------------------------------------------------------------------------------------------------
PA_AM_PAGES = 'https://www.lotteryusa.com/'
PA_AM_PICK3 = 'https://www.lotteryusa.com/pennsylvania/midday-pick-3/'
PA_AM_PICK4 = 'https://www.lotteryusa.com/pennsylvania/midday-pick-4/'

PA_PM_PAGES = 'https://www.lotteryusa.com/'
PA_PM_PICK3 = 'https://www.lotteryusa.com/pennsylvania/pick-3/'
PA_PM_PICK4 = 'https://www.lotteryusa.com/pennsylvania/midday-pick-4/'

P3_FECHA = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time'
P3_NU1 = "/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[1]/span"
P3_NU2 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span'
P3_NU3 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span'

P4_FECHA ='/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time'
P4_NU1 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[1]/span'
P4_NU2 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span'
P4_NU3 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span'
P4_NU4 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[4]/span'

PENNSYLVANIA_LOTTERYUSA = {

    'URL_MIDDAY'       : [PA_AM_PAGES,PA_AM_PICK3,PA_AM_PICK4],
    'URL_EVENING'       : [PA_PM_PAGES,PA_PM_PICK3,PA_PM_PICK4],

    "PICK3_MIDDAY"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_MIDDAY"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4],

    "PICK3_EVENING"     : [P3_FECHA,P3_NU1,P3_NU2,P3_NU3],
    "PICK4_EVENING"     : [P4_FECHA,P4_NU1,P4_NU2,P4_NU3,P4_NU4]
}

#! ----------------------------------------------------------------------------------------------------------------------------------

PENNSYLVANIA_TODO = [PENNSYLVANIA_LOTTERYUSA ]