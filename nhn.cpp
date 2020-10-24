//#include <iostream>
//#include <sstream>
//#include <vector>
//#include <algorithm>
//
//using namespace std;
//
//int dy[4] = { -1, 0, 1, 0 };
//int dx[4] = { 0, 1, 0, -1 };
//int tmp = 1;
//
//int dfs(int** arr, int N, int y, int x)
//{
//    arr[y][x] = 0;
//
//    for (int i = 0; i < 4; i++)
//    {
//        int ny = y + dy[i];
//        int nx = x + dx[i];
//        if ((0 <= ny) && (ny < N) && (0 <= nx) && (ny < N) && (arr[ny][nx] == 1))
//        {
//            tmp++;
//            dfs(arr, N, ny, nx);
//        }
//    }
//
//    return tmp;
//}
//
//int main()
//{
//    ios_base::sync_with_stdio(false);
//    cin.tie(NULL);
//
//    int N; // N 크기
//    cin >> N;
//
//    int **arr;
//    arr = (int **)malloc(sizeof(int *) * N);
//    for (int i = 0; i < N; i++)
//    {
//        arr[i] = (int *)malloc(sizeof(int) * N);
//    }
//
//    for (int i = 0; i < N; i++)
//    {
//        for (int j = 0; j < N; j++)
//        {
//            cin >> arr[i][j];
//        }
//    }
//
//    int cnt = 0;
//    vector<int> area;
//
//    for (int i = 0; i < N; i++)
//    {
//        for (int j = 0; j < N; j++)
//        {
//            if (arr[i][j] == 1)
//            {
//                cnt++;
//                tmp = 1;
//                area.push_back(dfs(arr, N, i, j));
//            }
//        }
//    }
//
//    sort(area.begin(), area.end());
//    cout << cnt << '\n';
//    for (int i = 0; i < area.size(); i++)
//    {
//        cout << area[i] << ' ';
//    }
//
//
//    for (int i = 0; i < N; i++) {
//        free(arr[i]);
//    }
//    free(arr);
//    return 0;
//}