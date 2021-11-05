
likers = ['Peter', 'Alex', 'John', 'Luke', 'Maggie', 'Monica', ]

def likes(names):
    names_len = len(names)
    """
    You probably know the "like" system from Facebook and other pages. 
    People can "like" blog posts, pictures or other items. We want to create 
    the text that should be displayed next to such an item.
    Implement the function which takes an array containing the names of people 
    that like an item. It must return the display text as shown in the examples:

    e.g

    []                                -->  "no one likes this"
    ["Peter"]                         -->  "Peter likes this"
    ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
    ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
    ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
    """
    if names_len == 0:
        return 'no one likes this'
    elif names_len == 1:
        return f'{names[0]} likes this'
    elif names_len == 2:
        return f'{names[0]} and {names[1]} like this'
    elif names_len == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    elif names_len >= 4:
        return f'{names[0]}, {names[1]} and {names_len-2} others like this'




likes(likers)


# * optimal solution

# check against minimum value between length of list and 4
# and access dict key. Will determine at which key to display message
# * likes_length-2 always returns the count of unmentioned people

def likes_2(names):
    likes_length = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    } [min(4, likes_length)].format(*names[:3], others=likes_length-2)

likes_len = len(likers)

likes_2(likers)

