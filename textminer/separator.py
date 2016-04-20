import re


def words(text):
    """ r'w*[^\s][a-zA-Z]+ passes the test, but it does not allow for one
     character words, so I added the | [a-zA-Z] """
    answer = re.findall(r'\w*[^\s][a-zA-Z]+|[a-zA-Z]+', text)
    if answer == []:
        return None
    return answer


def phone_number(pn):
    number_dict = {}
    try:
        area_code, part_1, part_2 = re.match(
            r'^\(*(\d{3})\)*[-|\s|\.]*(\d{3})[-|\s|\.]*(\d{4})', pn).groups()
        number_dict["area_code"] = area_code
        number_dict["number"] = "{}-{}".format(part_1, part_2)
        return number_dict
    except:
        return None


def money(c_string):
    money_dict = {}
    try:
        groups = re.match(r'^(\D)(\d+(,\d{3})*(\.\d{2})?)$', c_string).groups()
        money_dict["currency"] = groups[0]
        money_dict["amount"] = float(re.sub(r',', '', groups[1]))
        return money_dict
    except:
        return None


def zipcode(zc):
    zip_dict = {}
    try:
        zip_code, plus4 = re.match(r'^(\d{5})-*(\d{4})*$', zc).groups()
        zip_dict['zip'] = zip_code
        zip_dict['plus4'] = plus4
        return zip_dict
    except:
        return None


def date(date):
    date_dict = {}
    try:
        date_dict["year"] = int(re.search(r'(\d{4})', date).group())
        dict_date["month"] = int(re.search(r'^([0-9]{1,2})\D|\D([0-9]{1,2})\D', date).group())
        date_dict["day"] = int(re.search(r'(?=....\D([0-9]{1,2}))', date).group())
        return date_dict
    except:
        return False
