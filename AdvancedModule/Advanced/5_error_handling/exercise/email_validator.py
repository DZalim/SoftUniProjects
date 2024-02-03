class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


valid_domains = ('.com', '.bg', '.org', '.net')

email_to_validate = input()

while email_to_validate:
    name_check = email_to_validate.split('@')
    domain_check = email_to_validate.split('.')
    count_at_symbol = email_to_validate.count('@')
    if len(name_check[0]) <= 4:
        raise NameTooShortError('Name must be more than 4 characters')
    elif count_at_symbol != 1:
        raise MustContainAtSymbolError('Email must contain @ 1 time')
    elif f'.{domain_check[-1]}' not in valid_domains:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(domain for domain in valid_domains)}")
    else:
        print('Email is valid')

    email_to_validate = input()
