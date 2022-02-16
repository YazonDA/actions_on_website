**Stage - in the process of development**

The task of the Module is to automatically perform the specified actions on the site.

To describe actions,  the Module is use the YAML-file with following format:
1. At each next step, the Module:
   1. goes to a specified page,
   2. finds a specified marker
   3. Affects the found element (clicks on the link, writes data, etc.)

2. For each step, three fields are used:
   1. URL -- address of the page,
   2. Xpath -- link to the page element,
   3. DATA -- data or "code" of action.
