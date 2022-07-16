
#! ---------------------------------------------------------------------------------------------------------------------------------
FL_AM_PAGES = 'https://www.lotteryusa.com/'
FL_AM_PICK3 = ''
FL_AM_PICK4 = ''

FL_PM_PAGES = 'https://www.lotteryusa.com/'
FL_PM_PICK3 = ''
FL_PM_PICK4 = ''

FL_P3_FECHA = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time'
FL_P3_NU1 = "/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[1]/span"
FL_P3_NU2 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span'
FL_P3_NU3 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span'

FL_P4_FECHA ='/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time'
FL_P4_NU1 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[1]/span'
FL_P4_NU2 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span'
FL_P4_NU3 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span'
FL_P4_NU4 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[4]/span'

_LOTTERYUSA = {
    'URL_MIDDAY'       : [FL_AM_PAGES,FL_AM_PICK3,FL_AM_PICK4],
    'URL_EVENING'       : [FL_PM_PAGES,FL_PM_PICK3,FL_PM_PICK4],
    "PICK3_MIDDAY"     : [FL_P3_FECHA,FL_P3_NU1,FL_P3_NU2,FL_P3_NU3],
    "PICK4_MIDDAY"     : [FL_P4_FECHA,FL_P4_NU1,FL_P4_NU2,FL_P4_NU3,FL_P4_NU4 ],
    "PICK3_EVENING"     : [FL_P3_FECHA,FL_P3_NU1,FL_P3_NU2,FL_P3_NU3],
    "PICK4_EVENING"     : [FL_P4_FECHA,FL_P4_NU1,FL_P4_NU2,FL_P4_NU3,FL_P4_NU4 ]
}

#! ----------------------------------------------------------------------------------------------------------------------------------

_TODO = [_LOTTERYUSA ]