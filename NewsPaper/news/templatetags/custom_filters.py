from django import template


register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def censor_text(text):
   """
   value: значение, к которому нужно применить фильтр
   """
   # Возвращаемое функцией значение подставится в шаблон.
   if "редиска" in text:
      return (text.replace("редиска", "р******"))
   else: return text


@register.filter()
def censor_title(title):
   """
   value: значение, к которому нужно применить фильтр
   """
   # Возвращаемое функцией значение подставится в шаблон.
   if "редиска" in title:
      return (title.replace("редиска", "р******"))
   else: return title