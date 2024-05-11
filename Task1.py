def isEven(value):
  """
    Функция проверяет, является ли введенное число целым

    Args:
        value: объект для проверки

    Returns:
        Булево значение, если число целое, в противном случае выдает сообщение об ошибке
  """
    try:
      return (value & 1) == 0
    except:
      return "Value must be an integer"
