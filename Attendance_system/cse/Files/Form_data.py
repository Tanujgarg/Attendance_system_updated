A1_roll = [6315003, 6315004, 6315005, 6315006, 6315009, 6315010, 6315011, 6315012, 6315013, 6315014, 6315015, 6315016,
           6315017, 6315018, 6315021, 6315023, 6315024, 6315025]

A1_names = ['Gurdeep', 'Harmeet', 'Gurkirat', 'Riya', 'Navneet', 'Tanuj', 'Tarun', 'Vasu', 'Anshuman', 'Yogesh',
            'Zibran', 'Abhimanyu', 'Abhishek', 'Abhishek', 'Neha', 'Prerna', 'Priyanka', 'Ashish']

A2_roll = [6315002, 6315026, 6315027, 6315028, 6315029, 6315036, 6315037, 6315038, 6315039, 6315054, 6315056, 6315061,
           6315066, 6315067, 6315073, 6315076, 6315651, 6315654]

Cse1_roll = A1_roll + A2_roll

A2_names = ['Anmol', 'Anmol', 'Kajal', 'Chiranjeev', 'Dibyajyoti', 'Sabha', 'Sakshi', 'Sakshi', 'Samriti', 'Pankaj',
            'Parminder', 'Pulkit', 'Yogesh', 'Shubham', 'Simran', 'Vivek', 'Chanchal', 'Swapnil']

Cse1_names = A1_names + A2_names

A_key = ['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7', 'Student8', 'Student9',
         'Student10', 'Student11', 'Student12', 'Student13', 'Student14', 'Student15', 'Student16', 'Student17',
         'Student18']

Cse1_key = ['Student1', 'Student2', 'Student3', 'Student4', 'Student5', 'Student6', 'Student7', 'Student8', 'Student9',
            'Student10', 'Student11', 'Student12', 'Student13', 'Student14', 'Student15', 'Student16', 'Student17',
            'Student18', 'Student19', 'Student20', 'Student21', 'Student22', 'Student23', 'Student24', 'Student25',
            'Student26', 'Student27', 'Student28', 'Student29', 'Student30', 'Student31', 'Student32', 'Student33',
            'Student34', 'Student35', 'Student36']


A1_data = list(zip(A1_roll, A1_names, A_key))
A2_data = list(zip(A2_roll, A2_names, A_key))
Cse1_data = list(zip(Cse1_roll, Cse1_names, Cse1_key))

A3_roll = [6315008, 6315020, 6315022, 6315032, 6315035, 6315041, 6315043, 6315044, 6315045, 6315046,
           6315047, 6315048, 6315049, 6315050, 6315051, 6315053, 6315055, 6315057]

A3_names = ['Munisha', 'Arnav', 'Neha', 'Rashmi', 'Ruchika', 'Gaurav', 'Shivansh', 'Lakshay', 'Lovee',
            'Manan', 'Mridul', 'Nitesh', 'Satbeer', 'Shabnam', 'Shivani', 'Sunidhi', 'Paras', 'Prabhkirat']

A4_roll = [6315040, 6315052, 6315059, 6315060, 6315062, 6315064, 6315065, 6315068, 6315069, 6315070,
           6315071, 6315074, 6315077, 6315078, 6315652, 6315655, 6315658, 6315659]

A4_names = ['Ishan', 'Simran', 'Prashant', 'Pritech', 'Raju', 'Shekhar', 'Sahil', 'Anisha', 'Anish', 'Sant',
            'Sahil', 'Ishwar', 'Sunil', 'Udit', 'Gitashri', 'Swayam', 'Deepika', 'Anju']

Cse2_roll = A3_roll + A4_roll

Cse2_names = A3_names + A4_names

A3_data = list(zip(A3_roll, A3_names, A_key))
A4_data = list(zip(A4_roll, A4_names, A_key))
Cse2_data = list(zip(Cse2_roll, Cse2_names, Cse1_key))
