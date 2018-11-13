REST API Test Harness for Python unittest
=========================================

* [Python and Automated Testing](https://wiki.web.att.com/display/GCSDevOps/Python+and+Automated+Testing)

This **test harness** simplifies automated **REST API testing**.
The tests provide an **HTTP REST Client** to verify server _endpoints_.

Testing Stages
--------------

This library supports multiple *testing stages*, depending on which **unittest.TestCase** subclass is used.

* **Unit Testing with Mock Services**: The tests do not interact with live services.
* **QA or Regression Testing**: The tests interact with live, fully installed services.

QA or Regression Testing
------------------------

* [Python Requests Library](http://docs.python-requests.org/en/master/)

The **QA testing** relies on the **requests** library to form the **HTTP REST Client**.

The *Test Analyst* must understand **HTTP protocols** and how they apply to **REST APIs**.
