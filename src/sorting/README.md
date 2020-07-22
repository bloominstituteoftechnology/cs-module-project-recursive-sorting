# Merge Sort Logic

```py
merge(arr)
	initial array = [ 12 , 35, 87, 26, 9, 28, 7 ]
		/			                           \
	[12, 35, 87, 26]		              [9, 28, 7]
       /        \                             \     \
    [12, 35]  [87, 26]                     [9, 28]  [7]
          \      \     \     \       /    /      /
		[12] [35] [87]  [26]    [9]  [28]   [7]
		 |     |    |     |      |    |      |
		left right left right left  right  left
		/       \                   /         \
	   /         \                 /           \
      /           \               /             \
	[12, 35]      [26, 87]       [9, 28]      [7]
       |               |            |            |
       |               |            |            |
	new left	new right 	   new left      new right
		   /				             \
		  /                               \
		 /                                 \
        /                                   \
	[12, 26, 35, 87]                     [7, 9, 28]
		|                                   |
        |                                   |
		new left			             new right
			\                           /
	         \                         /
			  \                       /
			  [7, 9, 12, 26, 28, 35, 87]
              
# mergeHelper(arrA, arrB) 

# what does it return? 

# What are the arguments that this function takes in?

# Whatever this returns will become our new left and right, new left and right   always need to be a new array›◊
```
Courtesy of Iris Jitomo