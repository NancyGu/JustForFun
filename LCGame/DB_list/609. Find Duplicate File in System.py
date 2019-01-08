# 609. Find Duplicate File in System
from collections import defaultdict  # defaultdict可以避免key被访问却不存在的错误


# Step1: solved 2019-1-8 using hashmap
#
class Solution:
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        m = defaultdict(list)
        for p in paths:
            data = p.split()
            root = data[0]
            for v in data[1:]:
                name, content = v.split('(')
                content = content.split(')')[0]
                m[content].append(root + '/' + name)

        res = []
        for k in m:
            if len(m[k]) > 1:
                res.append(m[k])
        return res

# C++
'''
class Solution {
public:
    vector<vector<string>> findDuplicate(vector<string>& paths) {
        unordered_map <string,vector<string>> m;
        for(int i=0; i<paths.size(); i++){
            stringstream ss(paths[i]);
            
            string root;
            string s;
            // split
            getline(ss, root, ' ');
            
            while (getline(ss, s, ' ')) {
		        string fileName = root + '/' + s.substr(0, s.find('('));
		        string fileContent = s.substr(s.find('(') + 1, s.find(')') - s.find('(') - 1);
		        m[fileContent].push_back(fileName);
	        }
        }
        vector<vector<string>> res;
        for(auto x: m){
            if(x.second.size()>1)
                res.push_back(x.second);
        }
        return res;
    }
};
'''