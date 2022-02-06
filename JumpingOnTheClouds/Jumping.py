#Global Variables
ARRAY_SIZE = 10


def calculate_jumps(array):
   index = 0
   step_index = 0
   jumps =0

   while step_index <= len(array):
       step_index = index + 2
       
       if step_index >= len(array):
           break

       if array[step_index] == 1:
           step_index = step_index - 1;
           
       jumps = jumps + 1
       #print('Index', index, ' value: ', array[index], 'step_index', step_index, ' value: ', array[step_index])
       index = step_index

       
   return jumps


if __name__ == '__main__':
    array = [0,1,0,0,0,1,0]
    #array = [0,0,0,0,1,0]
    print(calculate_jumps(array))