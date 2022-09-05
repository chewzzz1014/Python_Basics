# write your code here
msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

msgs = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9]


def is_one_digit(v):
    if v > -10 and v < 10 and v.is_integer():
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    if not (msg == ""):
        msg = msg_9 + msg
    else:
        return None
    print(msg)


memory = 0
not_complete = True

while not_complete:
    operation = input(msg_0 + "\n").split()
    x = operation[0]
    y = operation[2]

    if x == "M":
        x = memory
    if y == "M":
        y = memory
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_1)
        continue

    oper = operation[1]
    if oper in ["+", "-", "*", "/"]:
        check(x, y, oper)
        if oper == "+":
            result = (x + y)
            print(result)
        elif oper == "-":
            result = (x - y)
            print(result)
        elif oper == "*":
            result = (x * y)
            print(result)
        elif (oper == "/") and (not y == 0):
            result = (x / y)
            print(result)
        else:
            print(msg_3)
            continue

        while True:
            to_store = input(msg_4 + "\n").strip()
            if to_store == "y":
                if is_one_digit(result):
                    msg_index = 10
                    while True:
                        ans = input(msgs[msg_index - 1])
                        if ans == "y":
                            if msg_index < 12:
                                msg_index += 1
                                continue
                            else:
                                memory = result
                                break
                        elif ans == "n":
                            break
                        else:
                            continue
                    else:
                        memory = result
                        break
            else:
                memory = result
                break
            elif to_store == "n":
            break
        else:
            continue

    while True:
        to_cont = input(msg_5 + "\n").strip()
        if to_cont == "y":
            break
        elif to_cont == "n":
            not_complete = False
            break
        else:
            continue

else:
    print(msg_2)

