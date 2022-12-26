from django import template

register = template.Library()


Banned_list = ['idiot', 'stupid', 'donkey']


@register.filter('censor')
def censor(sentence=''):
    new_sentence = ''

    for word in sentence.split():
        if word in Banned_list:
            new_sentence += '*(censored) '
        else:
            new_sentence += word + ' '

    return new_sentence


