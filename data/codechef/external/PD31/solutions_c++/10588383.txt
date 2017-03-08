#include <iostream>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <list>

using namespace std;

class Vertex
	{
		private:
			int id;
			int parent;
			list<Vertex*> nbrs;
			bool visited;
		
		public:
			Vertex(int a);
			void add_nbr(Vertex *b);
			int get_value();
			list<Vertex*> get_list();
			bool get_state();
			void set_state(bool states);
			void set_parent(int par);
			int get_parent();
				
	};

int Vertex::get_parent()
	{
		return parent;
	}

void Vertex::set_parent(int par)
	{
		parent=par;
	}

Vertex::Vertex(int a):id(a)
	{
		visited=false;
		parent=-871;
	}

bool Vertex::get_state()
	{
		return visited;
	}

void Vertex::set_state(bool states)
	{
		visited=states;
	}

void Vertex::add_nbr(Vertex *b)
	{
		nbrs.push_back(b);
	}	

int Vertex::get_value()
	{
		return id;
	}

list<Vertex*> Vertex::get_list()
	{
		return nbrs;
	}

class edge
	{
		private:
			int weight;
			Vertex *source;
			Vertex *destination;

		public:	
			edge(Vertex *sources,Vertex *destinations,int weigh);
			void set_weight(int a);
			int get_weight();
			Vertex* get_source();
			Vertex* get_destination();
		
	};

edge::edge(Vertex *sources,Vertex *destinations,int weigh)
	{
		weight=weigh;
		source=sources;
		destination=destinations;
	}

void edge::set_weight(int a)
	{
		weight=a;
	}

int edge::get_weight()
	{
		return weight;
	}

Vertex* edge::get_source()
	{
		return source;
	}

Vertex* edge::get_destination()
	{
		return destination;
	}

class Graph
	{
		private:
			list<Vertex> grf;
			list<edge> grf_edge;

		public:
			Graph();
			Vertex* get_vertex(int a);
			void add_edge(int a,int b);
			void add_vertex(int a);
			void prints();
			void dfs(int start);
			void bfs(int start);
			bool cycle(int start,int parents);
	};

bool Graph::cycle(int start,int parents)
	{
		
		Vertex *temp;
                temp=get_vertex(start);
		temp->set_parent(parents);
                stack<Vertex*> st;
                st.push(temp);
                while(!(st.empty()))
                        {
                                Vertex *top_ele;
                                top_ele=st.top();
                                st.pop();
                                if(!(top_ele->get_state()))
                                        {
                                   
                                                list<Vertex*> lsi;
                                                top_ele->set_state(true);
                                                lsi=top_ele->get_list();
                                                list<Vertex*>::iterator it;
                                                for(it=lsi.begin();it!=lsi.end();it++)
                                                        {
								if((*it)->get_state()&&(top_ele->get_parent()!=(*it)->get_value()))
									{
										return true;
									}
								st.push(*it);
								(*it)->set_parent(top_ele->get_value());
							}
                                        }

                        }
		list<Vertex>::iterator it;
		for(it=grf.begin();it!=grf.end();it++)
			{
				if(!(it->get_state()))
					return true;
			}
		return false;

	}

Graph::Graph()
	{}

void Graph::add_vertex(int a)
	{
		Vertex v(a);
		grf.push_back(v);
	}

void Graph::add_edge(int a,int b)
	{
		Vertex *temp_a,*temp_b;
		temp_a=get_vertex(a);
		temp_b=get_vertex(b);
		temp_a->add_nbr(temp_b);
		temp_b->add_nbr(temp_a);
		edge e1(temp_a,temp_b,1);
		edge e2(temp_b,temp_a,1);
		grf_edge.push_back(e1);
		grf_edge.push_back(e2);
	}

Vertex* Graph::get_vertex(int a)
	{
		 list<Vertex>::iterator it;

                for(it=grf.begin();it!=grf.end();it++)
                        {
                                if(it->get_value()==a)
                                        return &*it;
                        }
                add_vertex(a);
                return get_vertex(a);
	}

void Graph::prints()
	{
		list<Vertex>::iterator it;
                for(it=grf.begin();it!=grf.end();it++)
                        {
                                list<Vertex*>::iterator its;
                                list<Vertex*> temp;
                                temp=it->get_list();
                                cout << it->get_value() << " --> ";
                                for(its=temp.begin();its!=temp.end();its++)
                                        cout << (*its)->get_value() << " -->  ";
                                cout << endl;
                        }
	
	}

void Graph::dfs(int start)
	{
		Vertex *temp;
		temp=get_vertex(start);
		stack<Vertex*> st;
		st.push(temp);
		while(!(st.empty()))
			{
				Vertex *top_ele;
				top_ele=st.top();
				st.pop();
				if(!(top_ele->get_state()))
					{
						cout << top_ele->get_value() << " --> ";
						list<Vertex*> lsi;
						top_ele->set_state(true);
						lsi=top_ele->get_list();
						list<Vertex*>::iterator it;
						for(it=lsi.begin();it!=lsi.end();it++)
							st.push(*it);
					}
				
			}
	}

int main()
	{
		int n,m;
		cin >> n >> m;
		Graph g;
		while(m--)
			{
				int a,b;
				cin >> a >> b;
				g.add_edge(a,b);
				n=a;	
			}
		if(g.cycle(n,-1))
			cout << "NO" << endl;
		else
			cout << "YES" << endl;
	}
