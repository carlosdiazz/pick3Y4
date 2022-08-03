
def Mensaje_start(name):

    text  =      '<code>\nBOT LOTERIAS</code>\n\n'
    #text  +=     f'<b><u>Hola: {name}</u></b>\n'
    text  +=     f'<b>HOLA, {name}.</b>\n'
    text  +=     '<b>\nLOTERIA: </b> <i> GANAMAS </i>\n'
    text  +=     '<b>\nSORTEO: </b> <i> GANAMAS </i>\n'
    text  +=     '<b>\nFECHA: </b> <i> 12/12/2022 </i>\n'
    text  +=     '<b>Numeros Ganadores: </b> <i> 12-12-34 </i>'

    return text

def Mensaje_loteria(loteria, sorteo, fecha, numeros_ganadores):

    text  =      f'<code>\n -- <u>RESULTADOS</u> -- </code>\n\n'
    text  +=     f'<b>\nLOTERIA: </b><i> {loteria} </i>\n'
    text  +=     f'<b>\n SORTEO: </b><i> {sorteo} </i>\n'
    text  +=     f'<b>\n  FECHA: </b><i> {fecha} </i>\n'
    text  +=     f'<b>\nNUMEROS: </b><i> {numeros_ganadores["NU1"]}-{numeros_ganadores["NU2"]}-{numeros_ganadores["NU3"]} </i>'
    return text