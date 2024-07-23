def print_sample_invitation(mother, father, child, teacher, event):

    # Notice here the use of a multi-line format-string: f''' text here '''
    sample_text = f'''
Dear {mother} and {father},
    {teacher} and I would love to see you both as well as {child} at our {event} tomorrow evening. 

Best regards,
Principal G. Sturgis.
'''
    print(sample_text)


print_sample_invitation(mother='Karen', father='John', child='Noah', teacher='Tina', event='Pizza Party')
print_sample_invitation('Karen', 'John', 'Noah', 'Tina', 'Pizza Party')
# Both ways of function call is possible
# if we call a function and explicitly set the value of a parameter, the parameter is called "keyword parameter" or "named parameter"
# if only the value is specified then the parameter is called as "positional parameter"



# The content inside ''' ''' is the multi-line format string. 
# This means the string inside triple quotes each can span over multiple lines and also the result is formated as in the code.

