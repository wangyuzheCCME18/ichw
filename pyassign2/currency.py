"""Currency.py: Calculate amount of currency received in the given exchange.

__author__ = "Wang Yuzhe"
__pkuid__  = "1800011828"
__email__  = "1800011828@pku.edu.cn"
"""


def information_obtain(currency_from, currency_to, amount_from):
    """Obtain the information needed from the given website and transform
    the byte stream into a normal string.Extra robustness increased! :)"""
    currency_from = (currency_from.replace(' ', '')).upper()
    currency_to = (currency_to.replace(' ', '')).upper()
    amount_from = amount_from.replace(' ', '')
    from urllib.request import urlopen
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={currency_from}'
                  '&to={currency_to}&amt={amount_from}'.format(**{'currency_from': currency_from,
                                                                  'currency_to': currency_to,
                                                                  'amount_from': amount_from}))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr


def normal_input(jstr):
    """The given currency and amount all valid,process the string 'jstr' to get the
    amount of currency received in the given exchange."""
    for i in ['{', '}', '"']:
        jstr = jstr.replace(i, '')
    jstr = jstr.replace(':', ',')
    jstr = jstr.split(',')
    istr = jstr[3]
    istr = istr.split()
    return 'The amount of currency received in the given exchange is: '+istr[0]


def various_input(jstr, amount_from):
    """Judge whether the given currency and amount are valid.If so,calculate the
    amount of currency received in the given exchange.If not,remind the user
    to check up the input."""
    amount_from = amount_from.replace(' ', '')
    if '"success" : true' not in jstr:
        if 'Source currency code is invalid.' in jstr:
            return 'Sorry,the source currency code is invalid.'
        elif 'Exchange currency code is invalid.' in jstr:
            return 'Sorry,the exchange currency code is invalid.'
        elif 'Currency amount is invalid' in jstr:
            return 'Sorry,the currency amount is invalid.'
    elif float(amount_from) < 0:
        return 'Sorry,the amount of currency to convert must be a non-negative number.'
    else:
        return normal_input(jstr)


def exchange(currency_from, currency_to, amount_from):
    """Return the amount of currency received in the given exchange."""
    jstr = information_obtain(currency_from, currency_to, amount_from)
    return various_input(jstr, amount_from)


def test_information_obtain():
    """Test function information_obtain()."""
    assert information_obtain('USD', 'EUR', '2.5') == '{ "from" : "2.5 United States Dollars", "to" : ' \
                                                      '"2.1589225 Euros", "success" : true, "error" : "" }',\
        'Oh no,function information_obtain1 went wrong!'
    assert information_obtain('U S     D', '  EU    R', '   2    .   5') == '{ "from" : "2.5 United States Dollars", ' \
                                                                            '"to" : "2.1589225 Euros", "success" : ' \
                                                                            'true, "error" : "" }',\
        'Oh no,function information_obtain2 went wrong!'
    assert information_obtain('uSd', 'euR', '2.5') == '{ "from" : "2.5 United States Dollars", "to" : "2.1589225 ' \
                                                      'Euros", "success" : true, "error" : "" }',\
        'Oh no,function information_obtain3 went wrong!'


def test_normal_input():
    """Test function normal_input()."""
    assert normal_input('{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, '
                        '"error" : "" }') == 'The amount of currency received in the given exchange is: 2.1589225',\
        'Oh no,function normal_input1 went wrong!'
    assert normal_input('{ "from" : "567 Chinese Yuan", "to" : "71.458913763664 Euros", "success" : true, '
                        '"error" : "" }') == 'The amount of currency received in the given exchange is: ' \
                                             '71.458913763664',\
        'Oh no,function normal_input2 went wrong!'
    assert normal_input('{ "from" : "2.5 Chinese Yuan", "to" : "0.31507457567753 Euros", "success" : true, "error"'
                        ' : "" }') == 'The amount of currency received in the given exchange is: 0.31507457567753',\
        'Oh no,function normal_input3 went wrong!'


def test_various_input():
    """Test function various_input()."""
    assert various_input('{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }',
                         '2.5') == 'Sorry,the source currency code is invalid.',\
        'Oh no,function various_input1 went wrong!'
    assert various_input('{ "from" : "", "to" : "", "success" : false, "error" : "Exchange currency code is invalid." }'
                         '', '2.5') == 'Sorry,the exchange currency code is invalid.',\
        'Oh no,function various_input2 went wrong!'
    assert various_input('{ "from" : "", "to" : "", "success" : false, "error" : "Currency amount is invalid." }',
                         'abc') == 'Sorry,the currency amount is invalid.',\
        'Oh no,function various_input3 went wrong!'
    assert various_input('{ "from" : "-234 Euros", "to" : "-1856.7032860142 Chinese Yuan", "success" : true, '
                         '"error" : "" }', '-2.5') == 'Sorry,the amount of currency to convert must be a ' \
                                                      'non-negative number.',\
        'Oh no,function various_input4 went wrong!'


def test_exchange():
    """Test function exchange()."""
    assert exchange('CNY', 'EUR', '2.5') == 'The amount of currency received in the given exchange is: ' \
                                            '0.31507457567753',\
        'Oh no,function exchange1 went wrong!'
    assert exchange(' U s    D  ', 'eu    R', '  002  .  5 0 ') == 'The amount of currency received in the given ' \
                                                                   'exchange is: 2.1589225',\
        'Oh no,function exchange2 went wrong!'
    assert exchange('AAA', 'EUR', '2.5') == 'Sorry,the source currency code is invalid.',\
        'Oh no,function exchange3 went wrong!'
    assert exchange('USD', 'BBB', '2.5') == 'Sorry,the exchange currency code is invalid.',\
        'Oh no,function exchange4 went wrong!'
    assert exchange('USD', 'EUR', 'abc') == 'Sorry,the currency amount is invalid.',\
        'Oh no,function exchange5 went wrong!'
    assert exchange('USD', 'EUR', '-2.5') == 'Sorry,the amount of currency to convert must be a non-negative number.',\
        'Oh no,function exchange6 went wrong!'
    assert exchange('USD', 'CNY', '1024') == 'The amount of currency received in the given exchange is: 7016.5504',\
        'Oh no,function exchange7 went wrong!'
    assert exchange('EUR', 'CNY', '0.0000001024') == 'The amount of currency received in the given exchange is: ' \
                                                     '8.125060533669E-7',\
        'Oh no,function exchange8 went wrong!'


def test_all():
    """Test all cases."""
    test_information_obtain()
    test_normal_input()
    test_various_input()
    test_exchange()
    print("All tests passed")


def main():
    """Main Module."""
    test_all()
    currency_from = input('please type in the currency on hand: ')
    currency_to = input('please type in the currency to convert to: ')
    amount_from = input('please type in the amount of currency to convert: ')
    print(exchange(currency_from, currency_to, amount_from))


if __name__ == '__main__':
    main()
