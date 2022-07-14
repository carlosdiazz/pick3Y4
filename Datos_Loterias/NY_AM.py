NY_AM_PAGES     = 'https://www.lotteryusa.com/'
NY_AM_USA_PICK3 = 'https://www.lotteryusa.com/new-york/midday-numbers/'
NY_AM_USA_PICK4 = 'https://www.lotteryusa.com/new-york/midday-win-4/'

NY_P3_FECHA = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time'
NY_P3_NU1   = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[1]/span'
NY_P3_NU2   ='/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span'
NY_P3_NU3   ='/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span'

NY_P4_FECHA = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time'
NY_P4_NU1 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[1]/span'
NY_P4_NU2 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span'
NY_P4_NU3 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span'
NY_P4_NU4 = '/html/body/main/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[4]/span'

NEW_YORK_TARDE_LOTTERYUSA = {
    'URL' : [NY_AM_PAGES, NY_AM_USA_PICK3, NY_AM_USA_PICK4],
    'PICK3' : [NY_P3_FECHA,NY_P3_NU1,NY_P3_NU2,NY_P3_NU3 ],
    'PICK4' : [NY_P4_FECHA,NY_P4_NU1,NY_P4_NU2,NY_P4_NU3,NY_P4_NU4 ]
}

NEW_YORK_AM_TODO = [NEW_YORK_TARDE_LOTTERYUSA ]