for smth in 'a'*10:
    ID = ''
    lemma = ''
    form = ''
    tab_counter = 0
    i = 0
    user_input = input()
    if user_input != '':
        while tab_counter < 3:
            if user_input[i] == '\t':
                tab_counter = tab_counter + 1
            else:
                if tab_counter == 0:
                    ID = ID + user_input[i]
                if tab_counter == 1:
                    form = form + user_input[i]
                if tab_counter == 2:
                    lemma = lemma + user_input[i]
            i = i + 1
        my_cool_condition = lemma != form
        if user_input[0] == '#':
           my_cool_condition = False
        if my_cool_condition == True:
           print(form, lemma)
