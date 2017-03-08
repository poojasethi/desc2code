#include <iostream>
#include <algorithm>
#include <ctime>
#include <utility>
#include <stdlib.h>
#include <string.h>
using namespace std;

#define MOD 1000000000
#define MAX 400000
int n,q;

struct TreapNode {

	int key,priority,count;
	TreapNode *left, *right;

};

TreapNode* arrayT[MAX];

// A utility function to print tree
void inorder(TreapNode* root)
{

    if (root)
    {
       inorder(root->left);
        cout << "key: "<< root->key << " | priority: "
            << root->priority <<" | count "<< root->count;
        if (root->left)
            cout << " | left child: " << root->left->key;
        if (root->right)
            cout << " | right child: " << root->right->key;
        cout << endl;
        inorder(root->right);
    }
}


void update(TreapNode* s)
{	

	if(!s)
		return;

	int lc,rc;

	if(s->left==NULL)lc=0;
	else lc = s->left->count;

	if(s->right==NULL)rc=0;
	else rc = s->right->count;

	s->count = 1+rc+lc;

}

TreapNode* rr(TreapNode* y)
{
	TreapNode* x = y->left; 
	TreapNode* xr = x->right;

	x->right = y;
	y->left = xr;

	update(y);
	update(x);

	return x;

}

TreapNode* lr(TreapNode* x)
{
	TreapNode* y = x->right;
	TreapNode* yl = y->left; 

	y->left = x;
	x->right = yl;

	update(x);
	update(y);

	return y;

}

TreapNode* Node(int key)
{
	TreapNode* temp = new TreapNode;
	temp->key = key;
	int prior = 0;
    for(int i = 0; i < 10; i++)
        prior = (10LL * prior + rand() % 10) % MOD;

	temp->priority = prior;
	temp->right = NULL;
	temp->left = NULL;
	temp->count = 1;

	return temp;

}

TreapNode* search(TreapNode* root,int key)
{
	if(root==NULL||root->key==key)
		return root;

	if(root->key < key)
		return search(root->right,key);

	if(root->key > key)
		return search(root->left,key);

	return root;

}

TreapNode* insert(TreapNode* root,TreapNode* add)
{

	if(!root)
		return add;



	if(add->key <= root->key)
	{	
		root->left = insert(root->left,add);

		update(root->left);
		update(root);

		if(root->left->priority > root->priority)
			root = rr(root);

	}
	else
	{
		root->right = insert(root->right,add);

		update(root->right);
		update(root);

		if(root->right->priority > root->priority)
			root = lr(root);
	}

	//cout<<"Key :"<<root->key<<endl;

	return root;

}

pair<TreapNode*,TreapNode*> split(TreapNode* t, int key)
{

	TreapNode* temp = Node(key);
	temp->priority = MOD+1;

	TreapNode* root = insert(t,temp);

	
	return make_pair(root->left,root->right);

}

TreapNode* add(TreapNode* l,TreapNode* r)
{

	if(r)
	{	
		TreapNode *newadd = new TreapNode;
		newadd->priority = r->priority;
		newadd->key =  r->key;
		newadd->left=NULL;
		newadd->right=NULL;
		newadd->count=1;

		l = insert(l,newadd);

		/*
		cout<<"insert\n";
		inorder(l);
		cout<<"end insert\n";
		*/

		l = add(l,r->left);

		l = add(l,r->right);

		//cout<<"Key S :"<<l->key<<endl;

		return l;

	}
	
	return l;

}

TreapNode* unionS(TreapNode* l,TreapNode* r)
{

	if(l==NULL)
		return r;
	if(r==NULL)
		return l;

	if(l->count < r->count)
		swap(l,r);

	l = add(l,r);

	//cout<<"after Union :"<<l->key<<endl;

	/*
	cout<<"Changes add\n";
	inorder(l);
	cout<<"Visible now\n";
	*/

	return l;

}


TreapNode* unionT(TreapNode* l,TreapNode* r)
{
	if(l==NULL)
		return r;
	if(r==NULL)
		return l;

	if(l->priority < r->priority)
		swap(l,r);

	pair<TreapNode*,TreapNode*> eq;

	eq = split(r,l->key);

	TreapNode* node = Node(l->key);
	node->left = unionT(l->left,eq.first);
	node->right = unionT(l->right,eq.second);
	update(node->left);
	update(node->right);
	update(node);

	return node;

}


TreapNode* getkth(TreapNode* root,int num)
{
	int lc;
	if(root->left==NULL)lc=0;
	else lc = root->left->count;

	if(lc+1==num)return root;

	if(num< lc+1)
		return getkth(root->left,num);
	else if(num > lc+1)
		return getkth(root->right,num-(lc+1));

	return root;

}

int main()
{
	srand(time(NULL));
 
    scanf("%d%d",&n,&q);

    int unioncount=n+1;

    for(int i=1;i<=n;i++)
    {
    	arrayT[i]=Node(i);
    }

    for(int i=0;i<q;i++)
    {

    	char get[10];

    	scanf("%s",get);

    	int k1,k2;
   		 	
    	scanf("%d%d",&k1,&k2);

   		if(strcmp(get,"UNION")==0)
   		{
   			arrayT[unioncount]=unionS(arrayT[k1],arrayT[k2]);
   			//inorder(arrayT[unioncount]);
   			unioncount++;

   		}
   		else
   		{
   			printf("%d\n",getkth(arrayT[k1],k2)->key);
   		}

    }


}