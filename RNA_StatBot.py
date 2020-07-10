#imports 
import random 
import sys 
import time 

#class_[ribonucleic_acid]
class ribonucleic_acid_text:

    #init_[self//optional_parameters]
    def __init__(self):
        self.text = str(input('enter the rna sequence: '))
        self.text_list = list(self.text)

        #dictionaries
        self.base_dictionary = {
            'adenine':['a','A'],
            'uracil':['u','U'],
            'cytosine':['c','C'],
            'guanine':['g','G']
        }

    #def_[organize_input]
    def organize_input(self,RNA_input=None):
        RNA_input = self.text_list
        base_dictionary = self.base_dictionary
        self.CODON_input = []
        counter =int(0)

        #try_block
        try:
            #for_loop
            for item in RNA_input:

                codon = str(RNA_input[int(counter)] + RNA_input[int(counter+1)] + RNA_input[int(counter+2)])
                self.CODON_input.append(str(codon))
                counter +=int(3)
        #exception_block
        except Exception as ERROR:
            print(ERROR)
        print(self.CODON_input)

    #def_[codon_decryption]
    def codon_decryption(self):
        CODON_input = self.CODON_input
        base_dictionary = self.base_dictionary
        
        self.amino_acid_dictionary = {
            'phenylalanine':['UUU','uuu','UUC','uuc'],
            'leucine':['UUA','UUG','uua','uug','CUU','CUA','CUG','CUC','cuu','cua','cug','cuc'],
            'serine':['UCU','UCA','UCC','UCG','ucu','uca','ucc','ucg','AGU','AGC','agu','agc'],
            'tyrosine':['UAU','UAC','uau','uac'],
            'stop_codon':['UAA','UAG','uaa','uag','UGA','uga'],
            'cysteine':['UGU','UGC','ugu','ugc'],
            'tryptophan':['UGG','ugg'],
            'proline':['CCU','CCA','CCC','CCG','ccu','cca','ccc','ccg'],
            'histadine':['CAU','CAC','cau','cac'],
            'glutamine':['CAA','CAG','caa','cag'],
            'arginine':['CGU','CGA','CGG','CGC','cgu','cga','cgg','cgc','AGA','AGG','aga','agg'],
            'isoleucine':['AUU','AUC','AUA','auu','auc','aua'],
            'methionine':['AUG','aug'],
            'threonine':['ACU','ACC','ACG','ACA','acu','acc','acg','aca'],
            'asparagine':['AAU','AAC','aau','aac'],
            'lysine':['AAA','AAG','aaa','aag'],
            'valine':['GUA','GUG','GUC','GUU','gua','gug','guc','guu'],
            'alanine':['GCG','GCU','GCA','GCC','gcg','gcu','gca','gcc'],
            'aspartic_acid':['GAU','GAC','gau','gac'],
            'glutamic_acid':['GAA','GAG','gaa','gag'],
            'glycine':['GGG','GGA','GGU','GGC','ggg','gga','ggu','ggc']
            }
        print(self.CODON_INPUT)

if __name__ == str('__main__'):
    RNA_T = ribonucleic_acid_text()
    RNA_T.organize_input()
    RNA_T.codon_decryption()
