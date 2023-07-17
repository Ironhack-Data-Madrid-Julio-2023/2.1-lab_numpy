#1. Import the NUMPY package under the name np.

import numpy as np

#2. Print the NUMPY version and the configuration.

print('Version: ',np.__version__,'Configuration: ',np.show_config())


#3. Generate a 2x3x5 3-dimensional array with random values. Assign the array to variable "a"
# Challenge: there are at least three easy ways that use numpy to generate random arrays. How many ways can you find?

a = np.random.random((2,3,5))
a = np.ndarray((2,3,5))

#4. Print a.

print('\n')
print(a)


#5. Create a 5x2x3 3-dimensional array with all values equaling 1.
#Assign the array to variable "b"

b = np.zeros((5,2,3)) + 1

#6. Print b.

print('\n')
print(b)

#7. Do a and b have the same size? How do you prove that in Python code?

print('\n7: Yes they do, as the number of elements is both in the same case: 2*3*5.')
if a.size == b.size:
    print('Both arrays are the same size, which is '+str(a.size)+'.')
else:
    print('They are not the same size.')


#8. Are you able to add a and b? Why or why not?

try:
    np.add(a,b)
except ValueError:
    print('\n8: It is not possible because although they have the same number of elements, they do not have the same shape.')

#9. Transpose b so that it has the same structure of a (i.e. become a 2x3x5 array). Assign the transposed array to varialbe "c".

c = np.transpose(b,(1,2,0))

#10. Try to add a and c. Now it should work. Assign the sum to varialbe "d". But why does it work now?

try:
    d = np.add(a,c)
    print('\n10: Now it works because they have the same shape.')
    
except:
    print('\n10: It still does not work.')
    

#11. Print a and d. Notice the difference and relation of the two array in terms of the values? Explain.

print('\n')
print(a)
print('\n')
print(d)
print('\n')
print('11: They are different in one unit in every element. This is because the matrix c is a matrix of ones\
\n (just as b, which c comes from), so the result of a + c are the elements of a increased all by one.')



#12. Multiply a and c. Assign the result to e.

e = a*c


#13. Does e equal to a? Why or why not?

if np.array_equal(a, e):
    print('\n13: Yes, they are equal. This is because the one-to-one product applied to a to obtain e has been done with a matrix of ones, so every element will remain the same.')
else:
    print('\n14: What?! They are not equal...')
    

#14. Identify the max, min, and mean values in d. Assign those values to variables "d_max", "d_min", and "d_mean"

d_max = d.max()
d_min = d.min()
d_mean = d.mean()

print('\n')
display(d_max)
display(d_min)
display(d_mean)

#15. Now we want to label the values in d. First create an empty array "f" with the same shape (i.e. 2x3x5) as d using `np.empty`.

#16. Populate the values in f. For each value in d, if it's larger than d_min but smaller than d_mean, assign 25 to the corresponding value in f.

"""
If a value in d is larger than d_mean but smaller than d_max, assign 75 to the corresponding value in f.
If a value equals to d_mean, assign 50 to the corresponding value in f.
Assign 0 to the corresponding value(s) in f for d_min in d.
Assign 100 to the corresponding value(s) in f for d_max in d.
In the end, f should have only the following values: 0, 25, 50, 75, and 100.
Note: you don't have to use Numpy in this question.
"""


# Con bucles: ----------------------------------------------------------


f = np.empty((2,3,5))

for i in d:
    for j in i:
        for k in j:
            if k > d_min and k < d_max:
                f[np.where(d == k)] = 25
            elif k > d_mean and k < d_max:
                f[np.where(d == k)] = 75
            elif k == d_mean:
                f[np.where(d == k)] = 50
            elif k == d_min:
                f[np.where(d == k)] = 0
            elif k == d_max:
                f[np.where(d == k)] = 100
            else:
                pass

# Con .where, sin bucles : -----------------------------------------------

            
f = np.where(d == d_mean, 50, np.where(d == d_min, 0, np.where((d > d_min) & (d < d_mean), 25,\
    np.where((d > d_mean) & (d < d_max), 75,100))))


#17. Print d and f. Do you have your expected f?

"""
For instance, if your d is:
array([[[1.85836099, 1.67064465, 1.62576044, 1.40243961, 1.88454931],
        [1.75354326, 1.69403643, 1.36729252, 1.61415071, 1.12104981],
        [1.72201435, 1.1862918 , 1.87078449, 1.7726778 , 1.88180042]],

       [[1.44747908, 1.31673383, 1.02000951, 1.52218947, 1.97066381],
        [1.79129243, 1.74983003, 1.96028037, 1.85166831, 1.65450881],
        [1.18068344, 1.9587381 , 1.00656599, 1.93402165, 1.73514584]]])

Your f should be:
array([[[ 75.,  75.,  75.,  25.,  75.],
        [ 75.,  75.,  25.,  25.,  25.],
        [ 75.,  25.,  75.,  75.,  75.]],

       [[ 25.,  25.,  25.,  25., 100.],
        [ 75.,  75.,  75.,  75.,  75.],
        [ 25.,  75.,   0.,  75.,  75.]]])
"""

print('\n')
print(d)
print('\n')
print(f)
print('\n17: Yes, it is right.')


#18. Bonus question: instead of using numbers (i.e. 0, 25, 50, 75, and 100), how to use string values 
#("A", "B", "C", "D", and "E") to label the array elements? You are expecting the result to be:

g = np.where(d == d_mean, "C", np.where(d == d_min, "A", np.where((d > d_min) & (d < d_mean), "B",\
    np.where((d > d_mean) & (d < d_max), "D","E"))))

print('\n')
print(g)

"""
array([[[ 'D',  'D',  'D',  'B',  'D'],
        [ 'D',  'D',  'B',  'B',  'B'],
        [ 'D',  'B',  'D',  'D',  'D']],

       [[ 'B',  'B',  'B',  'B',  'E'],
        [ 'D',  'D',  'D',  'D',  'D'],
        [ 'B',  'D',   'A',  'D', 'D']]])
Again, you don't need Numpy in this question.
"""
