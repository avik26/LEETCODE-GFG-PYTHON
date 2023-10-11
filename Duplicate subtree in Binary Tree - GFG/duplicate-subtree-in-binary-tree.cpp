//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

struct Node
{
	char data;
	struct Node *left;
	struct Node *right;

	Node(char x) {
		data = x;
		left = NULL;
		right = NULL;
	}
};

struct Node* buildTree(string str)
{
	// Corner Case
	if (str.length() == 0 || str[0] == 'N')
		return NULL;

	// Creating vector of strings from input
	// string after spliting by space
	vector<string> ip;

	istringstream iss(str);
	for (string str; iss >> str; )
		ip.push_back(str);

	// Create the root of the tree
	Node *root = new Node(stoi(ip[0]));

	// Push the root to the queue
	queue<Node*> queue;
	queue.push(root);

	// Starting from the second element
	int i = 1;
	while (!queue.empty() && i < ip.size()) {

		// Get and remove the front of the queue
		Node* currNode = queue.front();
		queue.pop();

		// Get the current node's value from the string
		string currVal = ip[i];

		// If the left child is not null
		if (currVal != "N") {

			// Create the left child for the current Node
			currNode->left = new Node(stoi(currVal));

			// Push it to the queue
			queue.push(currNode->left);
		}

		// For the right child
		i++;
		if (i >= ip.size())
			break;
		currVal = ip[i];

		// If the right child is not null
		if (currVal != "N") {

			// Create the right child for the current node
			currNode->right = new Node(stoi(currVal));

			// Push it to the queue
			queue.push(currNode->right);
		}
		i++;
	}

	return root;
}


// } Driver Code Ends
/*The structure of the Binary Tree Node  is
struct Node
{
  char data;
  struct Node* left;
  struct Node* right;
};*/

/*The structure of the Binary Tree Node  is
struct Node
{
  char data;
  struct Node* left;
  struct Node* right;
};*/


vector <Node *> P;

int dfs(Node *root)
{   
//     cout << "in " << (int)root->data << endl;
    
    int l = 0, r = 0;
    if (root->left != NULL) {
        l = dfs(root->left);
    }
    if (root->right != NULL) {
        r = dfs(root->right);
    }
    
//     cout << "out " << (int)root->data << endl;
    int d = max(l, r);
    if (d == 1) P.push_back(root);
    return d+1;
}

class Solution {
  public:
    /*This function returns true if the tree contains 
    a duplicate subtree of size 2 or more else returns false*/
    int dupSub(Node *root) {
         P.clear();
         dfs(root);     
         
//          for (int i = 0; i < P.size(); i++) cout << (int)P[i]->data << endl;
         
         for (int i = 0; i < P.size(); i++) {
             for (int j = i+1; j < P.size(); j++) {
                 if (P[i]->data == P[j]->data) {
                     bool ok = true;
                     if (P[i]->left != NULL && P[j]->left == NULL) continue;
                     if (P[i]->left == NULL && P[j]->left != NULL) continue;
                     if (P[i]->right != NULL && P[j]->right == NULL) continue;
                     if (P[i]->right == NULL && P[j]->right != NULL) continue;
                     
                     if (P[i]->left != NULL) {
                         if ((P[i]->left)->data != (P[j]->left)->data) ok = false;
                     }        
                     if (P[i]->right != NULL) {
                         if ((P[i]->right)->data != (P[j]->right)->data) ok = false;
                     }
                     if (ok) return 1;
                 }
             }
         }
         return 0;
    }
};

//{ Driver Code Starts.

int main()
{
	
	int t;
	cin >> t;
	//cout << t << "\n";
	while (t--)
	{
		string treeString;
		getline(cin >> ws, treeString);
		struct Node* root = buildTree(treeString);
		Solution ob;
		cout << ob.dupSub(root) << "\n";
	}
	return 0;
}
// } Driver Code Ends