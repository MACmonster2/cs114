"""Reformat an all-digits phone number into xxx-xxx-xxxx and (xxx) xxx-xxxx."""
#1. Setup
#No setup

#2. Input
phone = input('Phone number? All digits. ')

#3. transform
#work on dependent steps first
has_area_code = len(phone) >7

#then slowly build up from the output you want
if has_area_code:
    phone_parts = [phone[:3], phone[3:6], phone[6:]]
else:
    phone_parts = [phone[:3], phone[3:]]

dashed_phone = '-'.join(phone_parts)
if has_area_code:
    fancy_phone = '({}) {}-{}'.format(phone_parts[0], phone_parts[1], phone_parts[2])
else:
    fancy_phone = dashed_phone

#4. Output
print(dashed_phone)
print(fancy_phone)
