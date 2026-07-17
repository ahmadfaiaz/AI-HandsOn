### 0:00:00 Introduction
        0:00:00 Exam Guide
        0:6:59 Exam Guide - What does it take to pass the exam?
        0:7:52 Exam Guide - Content Outline
        0:10:27 Exam Guide - Passing Grade
        0:11:11 Exam Guide - Question/Answer Types
        0:12:22 Exam Guide - Duration
        0:34:30 Setup Codebase Gitpod AWS CLI + AWS Account/Users (for Follow Along/Lab)
### 0:34:47 Setup
### 0:52:38 Amazon S3
        0:52:25 Amazon S3 (Simple Storage Service)
        0:54:11 S3 - CLI Follow Along
        5:06:32 S3 - Bucket Overview
        5:08:06 S3 - Bucket Naming Rules
        5:11:05 S3 - Bucket Naming Rules Examples
        5:12:54 S3 - Bucket Restrictions & Limitations
        5:15:54 S3 - Bucket Types
        5:18:53 S3 - Bucket Folders
        5:18:53 S3 - Bucket Folders
        5:21:04 S3 - Object Overview
        5:22:39 S3 - Object ETags
        5:24:26 S3 - Object ETags Follow Along
        5:43:01 S3 - Object Checksums
        5:44:11 S3 - Object Checksums Follow Along
        6:07:54 S3 - Object Prefixes
        6:09:12 S3 - Object Prefixes Follow Along
        6:21:27 S3 - Object Metadata
        6:22:41 S3 - Object Metadata (System Defined)
        6:24:03 S3 - Object Metadata (User Defined)
        6:25:15 S3 - Object Metadata Follow Along
        6:32:51 WORM (Write Once Read Many)
        6:33:52 S3 - Object Lock
        6:35:44 S3 - Bucket URI
        6:36:41 S3 - CLI
        6:39:19 S3 - Request Styles
        6:41:05 S3 - Dualstack Endpoints
        6:42:44 S3 - Storage Classes Overview
        6:47:09 S3 - Storage Classes - Standard
        6:49:14 S3 - Storage Classes - RRS (Reduced Redundancy Storage) [Legacy]
        6:50:43 S3 - Storage Classes - Standard-IA (Infrequent Access)
        6:52:38 S3 - Storage Classes Follow Along
        6:57:40 S3 - Storage Classes - Express One Zone [New]
        6:59:27 S3 - Storage Classes - One-Zone-IA
        7:01:44 'S3 Glacier Storage Classes' vs 'S3 Glacier "Vault"'
        7:04:49 S3 - Storage Classes - Glacier Instant Retrieval
        7:06:52 S3 - Storage Classes - Glacier Flexible Retrieval [<- Glacier "Vault"]
        7:10:33 S3 - Storage Classes - Glacier Deep Archive [<- Glacier "Vault"]
        7:11:50 S3 - Storage Classes - Intelligent-Tiering
        7:13:49 S3 - Storage Classes - Cheat Sheet
        7:17:38 S3 - Security - Overview
        7:22:11 S3 - Security - Block Public Access
        7:24:09 S3 - Security - ACL (Access Control Lists) [Legacy]
        7:25:35 S3 - Security - ACL Follow Along
        7:54:45 S3 - Security - Bucket Policies
        7:56:41 S3 - Security - Bucket Policies Follow Along
        8:08:51 S3 - Security - Bucket Policies vs IAM Policies
        8:10:54 S3 - Security - Access Grants
        8:12:22 S3 - Security - IAM Access Analyzer for S3
        8:13:23 S3 - Security - Internetwork traffic privacy
        8:15:41 CORS (Cross-Origin Resource Sharing)
        8:17:44 S3 - Security - CORS
        8:19:34 S3 - Security - CORS Follow Along
        9:06:51 S3 - Security - Encryption Overview
        9:07:59 S3 - Security - Encryption - In-Transit
        9:09:46 S3 - Security - Encryption - Server-Side Encryption
        9:11:19 S3 - Security - Encryption - Server-Side Encryption - SSE-S3
        9:12:48 S3 - Security - Encryption - Server-Side Encryption - SSE-KMS
        9:14:44 S3 - Security - Encryption - Server-Side Encryption - SSE-C
        9:16:39 S3 - Security - Encryption - Server-Side Encryption - DSSE-KMS
        9:19:23 S3 - Security - Encryption - Server-Side Encryption Follow Along
        9:56:37 S3 - Security - Encryption - Bucket Key
        9:59:16 S3 - Security - Encryption - Client-Side Encryption
        10:00:58 S3 - Security - Encryption - Client-Side Encryption Follow Along
        10:12:10 S3 - Data Consistency
        10:13:54 S3 - Object Replication
        10:15:15 S3 - Versioning
        10:16:32 S3 - Object Lifecycle
        10:18:19 S3 - Transfer Acceleration
        10:19:47 S3 - Presigned URL
        10:20:34 S3 - Presigned URL - Anatomy
        10:21:22 S3 - Access Points (smaller Bucket Policy)
        10:22:47 S3 - Multi-Region Access Points
        10:24:10 S3 - Object Lambda Access Points
        10:25:45 S3 - Mountpoint (Linux file system)
        10:27:48 S3 - Archived Objects
        10:29:50 S3 - Requesters Pay
        10:31:24 S3 - Requesters Pay - Header
        10:32:11 S3 - Requesters Pay - Troubleshooting
        10:33:12 AWS Marketplace for S3
        10:35:30 S3 - Batch Operations
        10:36:33 Amazon S3 Inventory
        10:37:30 S3 - Select
        10:39:27 S3 - Event Notifications
        10:40:58 S3 Storage Class Analysis
        10:42:30 S3 Storage Lens
        10:43:31 S3 - Static Website Hosting
        10:45:23 S3 - Multipart Upload
        10:47:44 S3 - Multipart Download (Byte Range Fetching)
        10:49:44 S3 Interoperability
        10:51:45 AWS API
        10:55:16 AWS CLI
        10:58:39 Access Keys
        11:03:15 API Retries and Exponential Backoff
        11:05:05 Smithy (AWS open-source IDL -> Service Model)
        11:06:22 STS (Security Token Service)
        11:08:41 STS AssumeRole Follow Along
        11:54:12 Signing AS API Requests
        11:56:02 AWS Signature Version 4
        11:58:01 AWS Service IP Address Ranges
        11:59:12 Service Endpoints
        12:01:58 AWS CLI - accepting input from file CLI Input Flag (--cli-input-json|yaml)
        12:02:49 Configuration Files (~/.aws/credentials|config)
        12:04:40 AWS CLI - Named Profiles
        12:06:10 AWS CLI - Configure Commands / SSO
        12:08:02 AWS CLI - Environment Variables
        12:11:15 AWS CLI - Autoprompt/Autocompletion
### 10:52:02 AWS API
### 12:19:52 VPC
        12:19:34 VPC
        12:21:36 Core Components of VPC
        12:24:09 Key Features of VPC
        12:26:09 VPC Follow Along
        13:41:24 Default VPC
        13:44:15 Deleting VPC
        13:45:05 Default Route (Catch-All-Route) 0.0.0.0/0 ::/0
        13:46:41 Delete & Recreate Default VPC Follow Along
        13:48:30 Shared VPC via RAM (sharing subnet)
        13:50:05 Shared VPC Follow Along
        14:09:06 NACLs
        14:12:28 NACL Follow Along
        15:10:40 Security Groups
        15:15:40 Security Groups Follow Along
        15:24:02 Stateless vs Stateful
        15:28:36 Route Tables
        15:35:28 Route Tables Follow Along
        15:37:58 Gateways
        15:42:57 IGW (Internet Gateway)
        15:44:29 IGW Follow Along
        15:47:12 EO-IGW (Egress-Only Internet Gateway)
        15:48:26 EO-IGW Follow Along
        16:07:47 EIP (Elastic IPs)
        16:13:17 EIP Follow Along
        16:18:40 AWS IPv6 Support
        16:19:51 Migrating from IPv4 to IPv6
        16:21:11 Direct Connect
        16:27:12 VPC Endpoints
        16:28:48 Private Link
        16:31:48 Interface Endpoints (powered via PrivateLink)
        16:33:34 GWLB (Gateway Load Balancer) Endpoint (powered via PrivateLink)
        16:35:09 VPC Gateway Endpoints (private to S3 & DynamoDB)
        16:36:09 VPC Endpoints Comparison
        16:38:56 VPC Flow Logs
        16:40:51 AWS VPN (Virtual Private Network)
        16:42:01 AWS Site-to-Site VPN
        16:46:07 VGW (Virtual Private Gateway)
        16:47:32 Customer Gateway
        16:49:59 TGW (Transit Gateway)
        16:50:56 AWS Client VPN
        16:53:14 NAT (Network Address Translation)
        16:54:50 NAT Gateway
        16:58:25 NAT Instances
        17:00:07 Jumpbox/Bastion host
        17:02:37 VPC Lattice
        17:06:07 TGW (Transit Gateway) More Detail
        17:09:07 Traffic Mirroring
        17:10:10 AWS Network Firewall
        17:11:33 VPC Peering
        17:14:16 VPC Peering Follow Along
        17:30:26 Network Address Usage
### 17:33:42 IAM
        17:34:43 AWS Managed vs Customer Managed vs Inline Policy
        17:36:00 Types of Policies Follow Along
        17:54:04 Anatomy of an IAM Policy
        17:56:06 Principle of least Privilege (PoLP)
        17:58:21 IAM Policy Follow Along
        18:42:30 AWS Account Root User
        18:45:50 IAM Password Policy
        18:46:19 IAM Password Policy Follow Along
        18:47:32 IAM Access Keys
        18:48:19 IAM Access Keys Follow Along
        18:52:56 IAM MFA (Multi-factor Authentication)
        18:53:52 IAM MFA (Multi-factor Authentication) Follow Along
        18:58:52 IAM Temporary Security Credentials
        19:00:08 IAM Identity Federation
        19:02:20 IAM STS (Security Token Service)
        19:04:36 IAM STS (Security Token Service) Follow Along
        19:09:11 IAM Cross Account Roles
        19:10:33 IAM AssumeRoleWithWebIdentity
        19:12:23 AWS SSO (Sign-Sign-On)
### 19:14:03 EC2
        19:15:29 Cloud Init
        19:17:22 Cloud Init Follow Along
        19:28:23 EC2 UserData
        19:30:41 EC2 UserData Follow Along
        19:43:55 EC2 Metadata
        19:48:44 EC2 Metadata Follow Along
        19:59:41 EC2 Instance Types
        20:01:50 EC2 Instance Family
        20:05:57 EC2 Instance Family Follow Along
        20:10:18 EC2 Processors
        20:13:53 EC2 Instance Sizes
        20:15:18 EC2 Instance Profile
        20:17:29 EC2 Instance Lifecycle
        20:20:37 EC2 Instance Console Screenshot
        20:21:28 EC2 Hostnames
        20:24:16 EC2 Default Username
        20:25:56 EC2 Burstable Instances
        20:29:15 EC2 Source & Destination Checks    
                - Source/Destination Check Enabled: EC2 handles only its own traffic.
                - Source/Destination Check Disabled: EC2 can forward traffic for other machines.
                - NAT: Allows private servers to access the internet without being accessible from the internet.
                - NAT Instance: An EC2 acting as a NAT device; Source/Destination Check must be disabled.
                - NAT Gateway: AWS-managed NAT service for private subnets to access the internet.
        20:30:03 EC2 System Log
                - Cloud init log useful
        20:31:37 EC2 Placement Groups
                - Cluster - no multi AZ - pack instances close in an AZ - low latency
                - Partition - placed in diff partition - large distributed replicated workload
                - Spread - placed in diff rack - separate critical instances - multi AZ - spread 7 instances
        20:32:42 Connecting to EC2 Instance
                - SSH Client - using public and private key - port 22 - SG should allow port 22
                        - cli - export *3
                        - cli - gp env *3
                        - ssh command - ssh-keygen -t rsa -f mynew_key
                        - command - aws ec2-instance-connect send-ssh-public-key...
                        - chmod 400 public key
                        - ssh -i ec2connect ec2-user@<public_key>
                - EC2 Instance connect - short live SSH key control by IAM work - only for linux
                - Session Manager - connect via a reverse connection - no port needed - controlled by IAM - give permission to audit tail of logins
                        - ** sudo passwd root - to create new password **
                - Fleet manager remote desktop - connect to windows machine using RDP - web browser
                - EC2 serial console - direct access to troubleshoot hardware layer
        20:35:54 Connecting to EC2 Instance Follow Along
        20:47:49 RDP (Remote Desktop Protocol) Follow Along
        20:57:12 EC2 Serial Console Follow Along
        21:07:27 EC2 Amazon Linux
        21:13:03 AMIs (Amazon Machine Image)
                - System manager automation - update patches
        21:25:43 AMIs (Amazon Machine Image) Follow Along (encrypted, copying to another region)
        21:36:48 ASG (Auto Scaling Groups)
        21:39:08 Capacity Settings
        21:40:22 Health Check Replacements
        21:41:41 ELB Integration
        21:42:29 Dynamic Scaling Policies
        21:43:35 Simple Scaling Policy
        21:45:21 Step Scaling Policy
        21:46:32 Target Tracking Scaling Policy
        21:47:45 Predictive Scaling Policy
        21:49:00 Termination Policies
        21:49:52 ELB (Elastic Load Balancer)
        21:51:49 The Rules of Traffic
        21:53:18 ALB (Application Load Balancer)
        21:55:17 NLB (Network Load Balancer)
        21:56:15 CLB (Classic Load Balancer)
### 21:13:27 AMIs
### 21:37:10 ASG
### 21:50:14 ELB
21:57:20 Route53
22:19:29 AWS Global Accelerator
22:21:00 CloudFront
22:30:24 EBS
22:45:34 EFS
22:50:38 FSx
22:54:24 AWS Backup
22:56:29 AWS Snow Family
23:07:07 AWS Transfer Family
23:09:31 AWS Migration Hub
23:15:35 AWS Data Sync
23:24:17 DMS
23:59:42 AWS Auto Scaling
24:16:59 AWS Amplify
24:37:15 Amazon AppFlow
24:53:39 AppSync
25:18:48 AWS Batch
25:46:37 OpenSearch Service
26:09:43 Device Farm
26:22:11 QLDB
26:24:01 Elastic Transcoder
26:52:21 AWS MediaConvert
27:02:09 SNS
27:43:05 SQS
28:44:00 Amazon MQ
29:32:34 Service Catalog
29:40:04 CloudWatch and EventBridge
30:16:36 Lambda
31:49:51 AWS Step Functions
32:48:57 AWS Compute Optimizer
32:59:19 Elastic Beanstalk
34:32:38 Kinesis
34:59:52 ElastiCache
35:51:13 MemoryDB
36:21:52 CloudTrail
37:19:23 Redshift
37:37:50 Athena
37:53:46 ML Managed Services
40:43:04 AWS Data Exchange
40:47:11 AWS Glue
41:27:04 Lake Formation
41:29:41 API Gateway
41:44:09 RDS
42:56:19 Aurora
43:33:29 DocumentDB
44:29:11 DynamoDB
45:10:04 Amazon Keyspaces
45:17:30 Neptune
45:35:00 ECR
45:39:18 ECS
46:02:27 EKS Cloud
46:21:45 KMS
46:32:00 AWS Audit Manager
46:40:23 ACM
46:58:57 Cognito
47:08:33 Amazon Detective
47:16:42 AWS Directory Service
47:22:47 AWS Firewall Manager
47:29:18 AWS Inspector
47:39:57 Amazon Macie
47:49:00 AWS Security Hub
47:53:37 AWS Secrets Manager
48:35:40 AI Dev Tools
48:59:17 Amazon MSK
49:29:32 AWS Shield
49:33:29 AWS WAF
49:37:48 CloudHSM
49:41:59 AWS Guard Duty
49:46:10 Health Dashboards
49:47:42 AWS Artifact
49:50:33 Storage Gateway
50:10:55 EC2 Pricing model