def calculate_vat(price):
  pdv=0.2
  res=price*pdv
  return res


def usd_to_uah(amount):
  rate=39.5
  conv=amount/rate
  return conv


def monthly_salary(hours,rate):
  return hours*rate


def apply_discount(price,discount):
  new_price=price*(1-discount)
  return new_price


def profit(revenue,cost,tax):
  prof=(revenue-cost)*(1-tax)
  return prof


def weighted_average_price(prices,quantities):
  total=0
  for index,num in (enumerate(prices)):
      total+=prices[index]*quantities[index]
  q=sum(quantities)
  avg_wght=total/q
  return avg_wght


def calculate_wacc(equity,debt,cost_of_equity,cost_of_debt,tax_rate):
  wacc=equity*cost_of_equity/(equity+debt)+debt*cost_of_debt*(1-tax_rate)/(equity+debt)
  return wacc


def monthly_payment(present_value,rate,months):
  Payment=present_value/((1-(1+rate)^(-rate*months))/rate)
  return Payment


def analyze_prices(prices):
  minimal_price=min(prices)
  maximal_price=max(prices)
  avg_value=mean(prices)
  less_than_avg=0
  if prices<avg_value:
    less_than_avg+=1
  dct={"мінімальна ціна" : {minimal_price},
       "максимальна ціна" : {maximal_price},
       "середнє значення" : {avg_value},
       "кількість товарів дешевших за середнє" : {less_than_avg}}
  return dct