# # def double_it(num):
# #     # Doubling the number until it exceeds 100
# #     while num < 100:
# #          # Show the current value before doubling
# #         #  num *= 2
# #         #  print(f"Doubling: {num}")
         
# #          if num * 2 > 100:
# #              print(f"final: {num}")
# #          else:
# #              print(num)
# #              break
        
          
# #     # return num

# # user_number = int(input("Enter a number to double it: "))
# # final_value = double_it(user_number)

# current = 2
# series = [current]

# while True:
#     next_num = current * 2
#     print(next_num) # still exceeds 100
#     if next_num < 100:
#         series.append(next_num)
#         current = next_num
#     else:
#         break

# print(series)


def double():
    
  num = float(input("Enter a number to double: "))
  
  while num * 2 < 100:
      num *= 2
      print(f"Doubled: {num}")
      

double()