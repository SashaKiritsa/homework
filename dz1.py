def parse_parameters(request: str) -> dict:

    dict_param = {}
    requestindex = request.find('?')
    if len(request[requestindex:]) != 1:
        request = request[requestindex + 1:]
        arr_parametrs = [s.split('=') for s in request.split('&')]
        dict_param = {s[0]: s[1] for s in arr_parametrs}
    return dict_param


def parse_cookies(cookies: str) -> dict:

    dict_cookies = {}
    if cookies.find(';') != -1:
        arr_cookies = [s.split('=') for s in cookies[:-1].split(';')]
        dict_cookies = {s[0]: s[1] for s in arr_cookies}
    return dict_cookies


if __name__ == '__main__':
    # Tests for function "parse_parameters"
    assert parse_parameters('http://example.com/?') == {}
    assert parse_parameters('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret',
                                                                                             'color': 'purple'}
    assert parse_parameters('https://www.youtube.com/watch?v=mijjgJXFBZo') == {'v': 'mijjgJXFBZo'}
    assert parse_parameters('https://card.apple.com/apply/start?referrer=cid%3Dapy-200-100002') == \
           {'referrer': 'cid%3Dapy-200-100002'}
    assert parse_parameters(
        'https://www.google.com/webhp?hl=ru&ictx=2&sa=X&ved=0ahUKEwjR9vX8-7TtAhVpo4sKHfDKDp0QPQgI') == \
           {'hl': 'ru',
            'ictx': '2',
            'sa': 'X',
            'ved': '0ahUKEwjR9vX8-7TtAhVpo4sKHfDKDp0QPQgI',
            }
    assert parse_parameters('https://www.youtube.com/watch?v=VsjlqafrlFM') == \
           {'v': 'VsjlqafrlFM'}
    assert parse_parameters('https://www.youtube.com/watch?v=gIOi0SO6UDI') == {
        'v': 'gIOi0SO6UDI'}
    assert parse_parameters('https://megasport.ua/ru/brand/nike/?gclid=Cj0KCQiA5bz-BRD-ARIsABjT4ni0uZjy2X6AwXpIq6xH'
                            '5rjzoBLr1KPonNkuYx7PWvcbeF_mrrq8g4MaAtC_EALw_wcB') == \
           {'gclid': 'Cj0KCQiA5bz-BRD-ARIsABjT4ni0uZjy2X6AwXpIq6xH5rjzoBLr1KPonNkuYx7PWvcbeF_mrrq8g4MaAtC_EALw_wcB'}
    assert parse_parameters('https://rozetka.com.ua/?gclid=Cj0KCQiA5bz-BRD-ARIsABjT4niVa9U56gSlXFukeFFAO4w78GZi-Z'
                            '827gefhKLj4bjs1KCfZAGkzHMaAhJHEALw_wcB') == {
        'gclid': 'Cj0KCQiA5bz-BRD-ARIsABjT4niVa9U56gSlXFukeFFAO4w78GZi-Z827gefhKLj4bjs1KCfZAGkzHMaAhJHEALw_wcB'}
    assert parse_parameters('https://www.youtube.com/watch?v=SMEZtIATpkQ') == {
        'v': 'SMEZtIATpkQ'}

    # Tests for function "parse_cookies"
    assert parse_cookies('') == {}
    assert parse_cookies('name=Sasha;') == {'name': 'Sasha'}
    assert parse_cookies('name=Dima; color=white;') == {'name': 'Dima', 'color': 'white'}
    assert parse_cookies('value=12345; name=Sasha;') == {'value': '12345', 'name': 'Sasha'}
    assert parse_cookies('name=Roma;') == {'name': 'Roma'}
    assert parse_cookies('path=PATH;Content-type=text\html;') == {'path': 'PATH', 'Content-type': 'text\html'}
    assert parse_cookies('DOMAIN=domain_name;') == {'DOMAIN': 'domain_name'}
    assert parse_cookies('tasty_cookie=banana;') == {'tasty_cookie': 'banana'}
