def load_words(text):
    return text.split()
    
class Message(object):
    
    #Text: text cua message
    #Co 2 attributes: self.message_text va self.valid_words
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(text)

    #Dung de acess self.message_text ngoai class
    def get_message_text(self):
        return self.message_text

    #Dung de access self.valid_words ngoai class
    def get_valid_words(self):
        return self.valid_words[:]
    #Tao 1 dictionary map cac upercase letter voi lowercase letter cua no  
    def build_shift_dict(self, shift):
        
        lower_keys = list(string.ascii_lowercase)
        lower_values = list(string.ascii_lowercase)
        shift_lower_values = lower_values[shift:] + lower_values[:shift]
        
        upper_keys = list(string.ascii_uppercase)                 
        upper_values = list(string.ascii_uppercase)
        upper_shift_values = upper_values[shift:] + upper_values[:shift]

        full_keys = lower_keys + upper_keys
        full_values = shift_lower_values + upper_shift_values

        self.shift_dict = dict(zip(full_keys, full_values))
        return self.shift_dict        
        

    def apply_shift(self, shift):
        #
        new_msg = []
        for i in self.message_text:
            if i not in self.build_shift_dict(shift).keys():
                new_msg.append(i)
                continue
            else:
                new_msg.append(self.build_shift_dict(shift)[i])
        return ''.join(new_msg)

msg = Message('hello')
msg.apply_shift(3)

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message
        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)
        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        #pass #delete this line and replace with your code here
        self.shift = shift
        self.message_text = text
        self.valid_words = load_words(text)
        self.encrypting_dict = super(PlaintextMessage, self).build_shift_dict(shift)
        self.message_text_encrypted = super(PlaintextMessage, self).apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        #pass #delete this line and replace with your code here
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        #pass #delete this line and replace with your code here
        encrypting_dict_copy = self.encrypting_dict.copy()
        return encrypting_dict_copy

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        #pass #delete this line and replace with your code here
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26
        Returns: nothing
        '''
        #pass #delete this line and replace with your code here
        self.shift = shift
        self.encrypting_dict = super(PlaintextMessage, self).build_shift_dict(shift)
        self.message_text_encrypted = super(PlaintextMessage, self).apply_shift(shift)

PlaintextMessage('Hello', 3)