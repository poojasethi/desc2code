#include <algorithm>
#include <cstdio>
#include <cstring>
#include <vector>
#include <set>

using namespace std;

const int MAX_N = 10;
const int N = 7;
const int M = 8;
const int MAX_COLORS = 4;
const int MAX_PAIRS = 10;
const char COLORS[MAX_PAIRS] = {'B', 'R', 'W', 'Y'};

int sol = -1, unmatched_pairs, configs;
char map[MAX_N][MAX_N];
int color_index[MAX_N][MAX_N];
int total[MAX_PAIRS], sum[MAX_PAIRS+1];
vector<int> cnt(MAX_PAIRS);
int code[MAX_COLORS][MAX_COLORS];
int fits[MAX_PAIRS][MAX_PAIRS];
vector<int> graph[MAX_N*MAX_N];
int visited[MAX_N*MAX_N*MAX_N], parent[MAX_N*MAX_N*MAX_N];
set<vector<int> > hash;
char output[2*MAX_N][2*MAX_N], current_output[2*MAX_N][2*MAX_N], used[2*MAX_N][2*MAX_N];
pair<char, char> colors[MAX_PAIRS];
int new_colors[MAX_PAIRS*MAX_N*MAX_N];
int match[MAX_N*MAX_N], unmatched_color_type[MAX_N*MAX_N];

int DFS(int node, int marker) {
  if (visited[node] == marker) {
    return 0;
  }
  visited[node] = marker;
  for (size_t i = 0; i < graph[node].size(); ++i) {
    if (parent[graph[node][i]] == -1 || DFS(parent[graph[node][i]], marker)) {
      parent[graph[node][i]] = node;
      match[node] = graph[node][i];
      return 1;
    }
  }
  return 0;
}

int MaximumMatching() {
  int result = 0, marker = 0;
  memset(match, -1, sizeof(match));
  memset(parent, -1, sizeof(parent));
  memset(visited, 0, sizeof(visited));
  for (int i = 1; i <= unmatched_pairs; ++i) {
    ++marker;
    result += DFS(i, marker);
  }
  return result;
}

void Repaint(int x1, int y1, int x2, int y2, pair<char, char> new_color) {
  char other_color;
  if (new_color.first != output[x1][y1] &&
      new_color.first != output[x2][y2]) {
    other_color = new_color.first;
  } else {
    other_color = new_color.second;
  }

  if (output[x1][y1] != new_color.first &&
      output[x1][y1] != new_color.second) {
    output[x1][y1] = other_color;
  } else {
    output[x2][y2] = other_color;
  }
}

void RepaintBoth(int x1, int y1, int x2, int y2, pair<char, char> new_color) {
  output[x1][y1] = new_color.first;
  output[x2][y2] = new_color.second;
}

void ComputeBestColoring() {
  int score = 0;

  for (int i = 1; i <= MAX_PAIRS; ++i) {
    sum[i] = sum[i-1] + max(0, min(28, total[i-1]-cnt[i-1]));
  }

  unmatched_pairs = 0;
  for (int i = 0; i < MAX_PAIRS; ++i) {
    score += 2*min(cnt[i], total[i]);

    for (int j = 0; j < cnt[i]-total[i]; ++j) {
      ++unmatched_pairs;
      unmatched_color_type[unmatched_pairs] = i;
      for (int k = 0; k < MAX_PAIRS; ++k) {
        if (fits[i][k]) {
          for (int l = sum[k]; l < sum[k+1]; ++l) {
            graph[unmatched_pairs].push_back(l);
            new_colors[l] = k;
          }
        }
      }
    }
  }

  if (score + unmatched_pairs > sol) {
    score += MaximumMatching();
    if (score > sol) {
      sol = score;
      memcpy(output, current_output, sizeof(current_output));
      memset(used, 0, sizeof(used));
      vector<int> restore;

      for (int k = 1; k <= unmatched_pairs; ++k) {
        if (match[k] != -1) {
          int repainted = 0;
          ++cnt[new_colors[match[k]]];
          restore.push_back(new_colors[match[k]]);
          for (int i = 0; i < N && !repainted; ++i) {
            for (int j = 0; j < M && !repainted; ++j) {
              if (i < N-1 && !used[2*i+1][2*j] && output[2*i+1][2*j] == '|' &&
                  code[color_index[i][j]][color_index[i+1][j]] == unmatched_color_type[k]) {
                used[2*i+1][2*j] = 1;
                Repaint(2*i, 2*j, 2*i+2, 2*j, colors[new_colors[match[k]]]);
                repainted = 1;
              }
              if (j < M-1 && !used[2*i][2*j+1] && output[2*i][2*j+1] == '-' &&
                  code[color_index[i][j]][color_index[i][j+1]] == unmatched_color_type[k]) {
                used[2*i][2*j+1] = 1;
                Repaint(2*i, 2*j, 2*i, 2*j+2, colors[new_colors[match[k]]]);
                repainted = 1;
              }
            }
          }
        }
      }

      for (int k = 1; k <= unmatched_pairs; ++k) {
        if (match[k] == -1) {
          int repainted = 0;
          for (int i = 0; i < N && !repainted; ++i) {
            for (int j = 0; j < M && !repainted; ++j) {
              if (i < N-1 && !used[2*i+1][2*j] && output[2*i+1][2*j] == '|' &&
                  code[color_index[i][j]][color_index[i+1][j]] == unmatched_color_type[k]) {
                used[2*i+1][2*j] = 1;
                for (int l = 0; l < MAX_PAIRS; ++l) {
                  if (total[l]-cnt[l] > 0) {
                    RepaintBoth(2*i, 2*j, 2*i+2, 2*j, colors[l]);
                    ++cnt[l];
                    restore.push_back(l);
                    break;
                  }
                }
                repainted = 1;
              }
              if (j < M-1 && !used[2*i][2*j+1] && output[2*i][2*j+1] == '-' &&
                  code[color_index[i][j]][color_index[i][j+1]] == unmatched_color_type[k]) {
                used[2*i][2*j+1] = 1;
                for (int l = 0; l < MAX_PAIRS; ++l) {
                  if (total[l]-cnt[l] > 0) {  
                    RepaintBoth(2*i, 2*j, 2*i, 2*j+2, colors[l]);
                    ++cnt[l];
                    restore.push_back(l);
                    break;
                  }
                }
                repainted = 1;
              }
            }
          }
        }
      }

      for (size_t i = 0; i < restore.size(); ++i) {
        --cnt[restore[i]];
      }
    }
  }

  for (int i = 1; i <= unmatched_pairs; ++i) {
    graph[i].clear();
  }
}

int GetColorIndex(char c) {
  for (int i = 0; i < MAX_COLORS; ++i) {
    if (c == COLORS[i]) {
      return i;
    }
  }
  return 0;
}

void GenerateConfigurations(int x, int y, int prev_state, int current_state) {
  if (x == N) {
    if (prev_state == (1<<M)-1 && hash.find(cnt) == hash.end()) {
      hash.insert(cnt);
      ++configs;
      ComputeBestColoring();
    }
  } else {
    if ((prev_state&(1<<y)) == 0) {
      current_state += 1<<y;
      ++cnt[code[color_index[x-1][y]][color_index[x][y]]];
      current_output[2*x-1][2*y] = '|';
      if (y+1 == M) {
        GenerateConfigurations(x+1, 0, current_state, 0);
      } else {
        GenerateConfigurations(x, y+1, prev_state, current_state);
      }
      --cnt[code[color_index[x-1][y]][color_index[x][y]]];
      current_output[2*x-1][2*y] = '.';
    } else {
      if (x+1 != N) {
        if (y+1 == M) {
          GenerateConfigurations(x+1, 0, current_state, 0);
        } else {
          GenerateConfigurations(x, y+1, prev_state, current_state);
        }
      }

      if (y+1 < M && (prev_state&(1<<(y+1))) != 0) {
        current_state += 1<<y;
        current_state += 1<<(y+1);
        ++cnt[code[color_index[x][y]][color_index[x][y+1]]];
        current_output[2*x][2*y+1] = '-';
        if (y+2 == M) {
          GenerateConfigurations(x+1, 0, current_state, 0);
        } else {
          GenerateConfigurations(x, y+2, prev_state, current_state);
        }
        --cnt[code[color_index[x][y]][color_index[x][y+1]]];
        current_output[2*x][2*y+1] = '.';
      }
    }
  }
}

int main() {
#ifndef ONLINE_JUDGE
  freopen("e.in", "r", stdin);
#endif

  for (int i = 0; i < 2*N-1; ++i) {
    for (int j = 0; j < 2*M-1; ++j) {
      current_output[i][j] = '.';
    }
  }

  for (int i = 0; i < N; ++i) {
    fgets(map[i], MAX_N, stdin);
    for (int j = 0; j < M; ++j) {
      color_index[i][j] = GetColorIndex(map[i][j]);
      current_output[2*i][2*j] = map[i][j];
    }
  }

  int color_pairs = 0;
  for (int i = 0; i < MAX_COLORS; ++i) {
    for (int j = MAX_COLORS-1; j >= i; --j) {
      code[i][j] = code[j][i] = color_pairs;
      scanf("%d ", &total[color_pairs]);
      colors[color_pairs] = make_pair(COLORS[i], COLORS[j]);
      ++color_pairs;
    }
  }

  for (int i = 0; i < MAX_COLORS; ++i) {
    for (int j = 0; j < MAX_COLORS; ++j) {
      for (int k = 0; k < MAX_COLORS; ++k) {
        fits[code[i][j]][code[i][k]] = 1;
        fits[code[i][j]][code[k][j]] = 1;
      }
    }
  }

  GenerateConfigurations(0, 0, (1<<M)-1, 0);

  printf("%d\n", sol);
  for (int i = 0; i < 2*N-1; ++i) {
    for (int j = 0; j < 2*M-1; ++j) {
      printf("%c", output[i][j]);
    }
    printf("\n");
  }

  return 0;
}
