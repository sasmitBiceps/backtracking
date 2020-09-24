#include <iostream>

using namespace std;
const int n = 4;


bool ratMaze(bool grid[n][n], int x, int y, bool path[n][n]){
	if(x == n-1 && y == n-1 && grid[n-1][n-1]){
		path[0][0]=1;
		return true;
	}
	if(x<=n-1 && y<=n-1 && grid[x+1][y] && ratMaze(grid, x+1, y, path)){
		path[x+1][y]=1;
		return true;
	}
	if(y<=n-1 && x<=n-1 && grid[x][y+1] && ratMaze(grid, x, y+1, path)){
		path[x][y+1]=1;
		return true;
	}

	return false;
}

void solve(bool grid[n][n],bool path[n][n]){
	bool solution= ratMaze(grid, 0, 0, path);
	if(solution){
		for(int i=0; i<n; ++i){
			for (int j = 0; j<n; ++j)
			{
				cout<<path[i][j]<<" ";
			}
			cout<<endl;
		}
	}
	else{
		cout<<"No solution"<<endl;
	}
}

int main(){
	bool grid[n][n];
	bool path[n][n];
	for(int i=0; i<n; ++i){
		for(int j=0; j<n; ++j){
			cin>>grid[i][j];
			path[i][j]=0;
		}
	}
	solve(grid, path);

	return 0;
}