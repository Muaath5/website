#include <bits/stdc++.h>
#define ll long long
#define pii pair<int, int>
using namespace std;

const int N = 2e5+1;

int n;
string s[N];
int f[N];

int vals[5];
bool check_values() {
	int cnt = 0;
	for (int i = 0; i < n; i++) {
		int sum = 0;
		for (char c : s[i])
			sum += vals[c-'A'];
		if (sum == f[i]) cnt++;
	}
	if (cnt == 3) cerr << '#';
	return cnt == 5;
}

map<string, int> amino;
set<string> dis;

array<string, 5> names;
vector<array<string, 5>> sols;
void rec(int fixed, int idx=0) {
	if (idx == 5) {
		if (check_values()) {
				
			sols.push_back(names);
		}
		return;
	}
	if (idx == fixed) rec(fixed, idx+1);
	else {
		for (auto [am, we] : amino) {
			if (!dis.count(am)) {
				vals[idx] = we;
				names[idx] = am;
				// dis.insert(am);
				rec(fixed, idx+1);
				// dis.erase(am);
			}
		} 
	}
}

int main()
{
	ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> s[i] >> f[i];
		f[i] += 180;	
	}

	amino["alanine"] = 89;
	amino["arginine"] = 174;
	amino["asparagine"] = 132;
	amino["aspartic_acid"] = 133;
	amino["cysteine"] = 121;
	amino["glutamic_acid"] = 147;
	amino["glutamine"] = 146;
	amino["glycine"] = 75;
	amino["histidine"] = 155;
	amino["isoleucine"] = 131;
	amino["leucine"] = 131;
	amino["lysine"] = 146; 
	amino["methionine"] = 149;
	amino["phenylalanine"] = 165;
	amino["proline"] = 115;
	amino["serine"] = 105;
	amino["threonine"] = 119;
	amino["tryptophan"] = 204;
	amino["tyrosine"] = 181;
	amino["valine"] = 117;
	amino["water"] = 18;
	
	int q;
	cin >> q;
	while (q--) {
		char c;
		string x;
		cin >> c >> x;
		vals[c-'A'] = amino[x];
		names[c-'A'] = x;
		sols.clear();
		rec(c-'A');
		cout << sols.size() << " solutions\n";
		for (auto arr : sols) {
			for (int i = 0; i < 5; i++)
				cout << char('A'+i) << ": " << arr[i] << endl;
		}
	}
}
