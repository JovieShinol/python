"""Question 1 was based on string validation.

String is valid if it satisfies all the conditions.

at least 4 characters
no space or slash(/)
at least one numeric digit
at least one capital letter

starting character must not be a number"""

def string_challange(s):
    
    if len(s)>=4:
       
        for i in range(len(s)):
            if s[i] == " " or s[i] =="/":
                return 0
            else:
                
                if s[i].isdigit():
                    dig = 0
                    dig+=1
                    if s[i]>='A' or s[i]<='Z':
                        caps = 0
                        caps+=1
                    
                
        if dig > 0 and caps > 0:
            return "string accepted" 
        else:
            return 0
    else:
        return 0






string = "3Ansalr"

a = string_challange(string)
print(a)
