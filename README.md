# CS3030 Python Assignent 3 (hw9)
Did this add?
# Group Assignment:
	Group2 member's
		Bader Binsunbil
		Grace Borges
		Juan Santos

# DISCRIPTION:

	Module 1 Task 1 ===> minivan.py
	This modle is going to check if doors would open or not.

	Module 1 Task 2 ===> minivantest.py
	This module is going to test minivan.py using csv file data.


# FUNCTIONS:
	
	On minivan.py

	main()
		It will assign "R1" value to switch list in the first index which is index[0].
		It will take user input and assign it to the switch list.
		It will call testing method.
		It will call doors_lockers()

	doors_lockers()

		This function will check if the doors of the minivan is open or not using the following data:

		ld => left dashboard switch
		rd => right dashboard switch
		cl => child lock switch
		ml => master lock switch
		li => left inside handle
		lo => left outside handle
		ri => right inside handle
		ro => right outside handle

	On minivantest.py

	main()
		It will call testing method.

	testing()
		This function will test the minivan doors which they are open or not using getFile variable.
		It will open the file from the web.
		It will call doors function from minivan.py


