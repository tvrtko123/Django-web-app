from django.core.validators import RegexValidator


'''
This regex assumes that you have a clean string,
you should clean the string for spaces and other characters
'''

emailregexvalidator = RegexValidator(r'\S+@\S+\.\S+',
                             message='Must be a valid email',
                             code='Invalid')


correctURLvalidator = RegexValidator(r'^(https?:\/\/)?(www.)?cloud(\.)anylogic(\.)com(\/)assets(\/)embed(\?)modelId=([a-zA-Z0-9]){8}-([a-zA-Z0-9]){4}-([a-zA-Z0-9]){4}-([a-zA-Z0-9]){4}-([a-zA-Z0-9]){12}$',
                             message='Please insert a correct URL',
                             code='Invalid name')

isalphavalidator = RegexValidator(r'^([\w]*[\s]?)*$',
                             message='Hashtag name must be alphanumeric',
                             code='Invalid name')

