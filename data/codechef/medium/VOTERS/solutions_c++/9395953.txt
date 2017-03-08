#include<stdio.h>
#include<stdlib.h>

struct node
{
    int key;
    int count;
    struct node *left;
    struct node *right;
    int height;
};

int max(int a, int b);

int height(struct node *N)
{
    if (N == NULL)
        return 0;
    return N->height;
}

int max(int a, int b)
{
    return (a > b)? a : b;
}

struct node* newNode(int key)
{
    struct node* node = (struct node*)
            malloc(sizeof(struct node));
    node->key   = key;
    node->count =1;
    node->left   = NULL;
    node->right  = NULL;
    node->height = 1;  // new node is initially added at leaf
    return(node);
}

struct node *rightRotate(struct node *y)
{
    struct node *x = y->left;
    struct node *T2 = x->right;

    x->right = y;
    y->left = T2;

    y->height = max(height(y->left), height(y->right))+1;
    x->height = max(height(x->left), height(x->right))+1;

    return x;
}

struct node *leftRotate(struct node *x)
{
    struct node *y = x->right;
    struct node *T2 = y->left;

    y->left = x;
    x->right = T2;

    x->height = max(height(x->left), height(x->right))+1;
    y->height = max(height(y->left), height(y->right))+1;

    return y;
}

int getBalance(struct node *N)
{
    if (N == NULL)
        return 0;
    return height(N->left) - height(N->right);
}

struct node* insert(struct node* node, int key)
{
    if (node == NULL)
        return(newNode(key));

    if(node->key==key){
        node->count++;
        return node;
    }

    if (key < node->key)
        node->left  = insert(node->left, key);
    else
        node->right = insert(node->right, key);

    node->height = max(height(node->left), height(node->right)) + 1;

    int balance = getBalance(node);

    if (balance > 1 && key < node->left->key)
        return rightRotate(node);

    if (balance < -1 && key > node->right->key)
        return leftRotate(node);

    if (balance > 1 && key > node->left->key)
    {
        node->left =  leftRotate(node->left);
        return rightRotate(node);
    }

    if (balance < -1 && key < node->right->key)
    {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }

    return node;
}

int total=0;

void gettotal(struct node *root)
{
    if(root != NULL)
    {
        gettotal(root->left);

        if(root->count>1)
            total++;

        gettotal(root->right);
    }
}

void inorder(struct node *root)
{
    if(root != NULL)
    {
        inorder(root->left);

        if(root->count>1)
            printf("%d\n", root->key);

        inorder(root->right);
    }
}

int main()
{
    int a,b,c,temp;

    scanf("%d",&a);
    scanf("%d",&b);
    scanf("%d",&c);

    struct node *root = NULL;
    int i=0;

    for(i=0;i<a;i++){
        scanf("%d",&temp);
        root = insert(root, temp);
    }

    for(i=0;i<b;i++){
        scanf("%d",&temp);
        root = insert(root, temp);
    }

    for(i=0;i<c;i++){
        scanf("%d",&temp);
        root = insert(root, temp);
    }

    gettotal(root);

    printf("%d\n", total);

    inorder(root);

    return 0;
}
