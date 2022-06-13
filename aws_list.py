# This project is an aws-list to learn python in LUIT
# Create an empty list.
aws_list = []

#Populating the list using either append or insert functions.
aws_list.insert(0, 'EC2')
aws_list.append('Lambda')
aws_list.append('DynamoDB')
aws_list.append('RDS')
aws_list.append('S3')

# Printing the list
print("A list of AWS services is ", aws_list)

# Printing the length of the list
length_list = len(aws_list)
print("The # of AWS services is ", length_list)

# Now removing two items from the list  by name or index
aws_list.remove("RDS")
aws_list.remove("S3")

# Printing the new list with the new items removed
print("The updated list of AWS services is ", aws_list)
length_list = len(aws_list)
print("The updated # of AWS services is ", length_list)
