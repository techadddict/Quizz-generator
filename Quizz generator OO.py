import os
import random

class Quizz_Generator:
    def __init__(self,the_dictionary):
        self.my_dict=the_dictionary

    def create_folder(self,path):
        os.makedirs(path)
        return

    def get_dict_keys(self,my_dictionary):
        states_only= list(self.my_dict.keys())
        return states_only

    def get_dict_values(self,my_dictionary):
        capitals_only= list(self.my_dict.values())
        return capitals_only


    def create_write_to_files(self,number_of_files,number_of_questions,path,options):
        states_only= self.get_dict_keys(self.my_dict)
        capitals_only= self.get_dict_values(self.my_dict)
        for i in range(number_of_files):
            file=open(path + '/Quizz_' +str(i+1) + '.txt','a')
            file.write('Name:\n\nDate:\n\nClass:\n\n')
            file.write((' '* 20) + 'State Capitals Quiz (Form %s)' % (i + 1))
            file.write('\n')
            for i in range(number_of_questions):
                capitals_only_2=capitals_only.copy()
                random.shuffle(states_only)
                rand_state=states_only[i]
                capitals_only_2.remove(self.my_dict[rand_state])
                answers=list(random.sample(capitals_only_2,3))
                file.write(str(i+1) + '. '+ 'What is the capital city of ' + rand_state + '?')
                file.write('\n\n')
                answers.append(self.my_dict[rand_state])
                random.shuffle(answers)
                for i in range(len(answers)):
                    file.write(options[i])
                    file.write(answers[i])
                    file.write('\n')
                file.write('\n')




        file.close()




states_capital={
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'}


options=['A. ','B. ','C. ','D. ']
path='/Users/martingwarada/Desktop/Geography_QUIZES'
my_quizz_generator=Quizz_Generator(states_capital)
my_quizz_generator.create_folder(path)
my_quizz_generator.create_write_to_files(30,50,path,options)
