def calculations():
    number1= int(input("Enter first Number :"))
    number2= int(input("Enter second Number :"))
    sum=("Sum of {number1} and {number2} is  ", number1+number2)
    difference=("Difference of {number1} and {number2} is   ", number1-number2)
    product=("Product of {number1} and {number2} is  ", number1*number2)
    quotient=("The quotient of {number1}  and {number2} is   " , number1/number2)
    return sum,difference,product,quotient
result1_sum,result2_diff,result3_pro,result4_quo = calculations()
print(result1_sum, result2_diff, result3_pro ,result4_quo)