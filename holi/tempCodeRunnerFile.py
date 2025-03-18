# #include <iostream>
# using namespace std;
# int main()
# {
# 	int arr[] = {11,22,33,44,55,66,77,88,99,100,110};
# 	int s = sizeof(arr)/ (sizeof(arr[0]));
	
# 	cout<<"Before Delete: "<<endl;
# 	for( int i =0; i<s; i++) cout<<arr[i]<<" ";
# 	cout<<endl;
	
# 	int key;
# 	cout<<"Enter the value of key: ";

# 	cin>>key;
	
# 	if(key < s)
# 	{
# 		cout<<"To be delete: "<<arr[key]<<endl;
	
# 		for(int i = key; i<s; i++)
# 		{
# 			arr[i] = arr[i+1];
# 		}
# 		s--;
# 		cout<<"After Delete: "<<endl;
# 		for( int i =0; i<s; i++) cout<<arr[i]<<" ";
# 		cout<<endl;
# 	}
# 	else
# 	{
# 		cout<<"Index value is too large";
# 	}
	
	
# 	return 0;
# }