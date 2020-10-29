front_vow = "eiöü"
back_vow = "aıou"
wrong_vows = ''
latest_vow = '6' #символ не входящий в front_vow или back_vow

total_vowharmony = 0
total_novowharmony = 0

for smth in 'a'*5:
    my_cool_condition = False
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
        if len(form) > len(lemma):
            sym_index = 0
            form_beginning = ''
            for sym in lemma:
                form_beginning = form_beginning + form[sym_index]
                sym_index = sym_index + 1
            if form_beginning == lemma:
                my_cool_condition = True
            
        if user_input[0] == '#':
            my_cool_condition = False
         
        vowharmony = True
        if my_cool_condition == True:
            for phon in lemma:
                if phon in front_vow + back_vow:
                    latest_vow = phon
            if latest_vow in front_vow:
                wrong_vows = back_vow
            elif latest_vow in back_vow:
                wrong_vows = front_vow
            else:
                vowharmony = False

            while sym_index < len(form):
                if form[sym_index] in wrong_vows:
                    vowharmony = False
                sym_index = sym_index + 1
            
            if vowharmony == True:
                total_vowharmony = total_vowharmony + 1
            else:
                total_novowharmony += 1
        
print(total_vowharmony, total_novowharmony)
