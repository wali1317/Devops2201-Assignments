## This is AWS Cloud Formation Assignment no 1

### Lab 2.2.4: Using CloudFormation 

Q. Using cloudformation we need to create a bucket which satisfy following criteria:
    
- Create and assign an IAM policy to explicitly grant yourself maintenance access
- Set a bucket policy to grant read access
- Set a s3 acl on 'Private.txt' to block read access unless you are authenticated.

Ans. One template was written and pushed as s3template.yaml. Then from the command line the template 
was validated using the following command:

$ aws cloudformation validate-template --template-body file://s3template.yaml

After validating the template a stack was created named cfassignment1

$ aws cloudformation create-stack --stack-name cfassignment1 --template-body file://s3template.yaml

It was observed that a s3 bucket was created as named in yaml doc "izaan-wali1322".
Then two files were uploaded on s3 bucket namely test1.txt and private.txt.

$ aws s3 cp test1.txt s3://izaan-wali1322

$ aws s3 cp private.txt s3://izaan-wali1322

At the time of validation, test.txt file could be found using the url, where access was denied 
for private.txt

The url of test1.txt is https://izaan-wali1322.s3.amazonaws.com/test1.txt

The url of private.txt is https://izaan-wali1322.s3.amazonaws.com/private.txt

### Lab 2.3.1: Set up for Versioning

Q. Experiment with bucket versioning. Using the CLI, delete the bucket stack you created for 
Principle 2 so that we can start out fresh. Make a copy of the stack template you just wrote above, 
and modify it for this lab:

- Create the stack with versioning enabled on the bucket 
- Upload your local data files to the bucket with the CLI.
- Modify your local data files, and sync those files to the bucket again.
- Inspect your bucket's objects after syncing and see how many versions there are.
- Fetch the original version of an object.
- Delete one of the objects that you changed.

Ans. A template "s3vertemplate.yaml" was modified enabling the versioning of the bucket. Then from 
the command line the template was validated using the following command:

$ aws cloudformation validate-template --template-body file://s3vertemplate.yaml

After validating the template a stack was created named cfassignment1

$ aws cloudformation create-stack --stack-name cfassignment2 --template-body file://s3vertemplate.yaml

Then two files were uploaded on s3 bucket namely test1.txt and private.txt from the temp directory.

$ aws s3 cp test1.txt s3://izaan-wali1323

$ aws s3 cp private.txt s3://izaan-wali1323

Then above two files were modified by adding some lines with the help of vim text editor and 
synced temp directory with "izaan-wali1323" s3 bucket:

$ aws s3 sync . s3://izaan-wali1323

Then it was found that both of the files have two versions.

Then original version of test1.txt was downloaded by the following commands:

$ aws s3api list-object-versions --bucket izaan-wali1323 --prefix test1.txt

From the above command the version id was taken of the original version.

$ aws s3api get-object --bucket izaan-wali1323 --key test1.txt --version-id z6lnyVVwfSx7.g5OxVFT9v6mMWI5tY5j testorigine.txt

It was confirmed by cat command that testorigine.txt is same as the original version of test1.txt.

Then this file was deleted using following command:

$ aws s3api delete-object --bucket izaan-wali1323 --key test1.txt

It was observed that the file is available with delete marker

{
"DeleteMarker": true,

"VersionId": "HnCdaD1LRJJ2PgiSU1WOr2LtGZczntJr"
}

Q. Can you still retrieve old versions of the object you removed?

Ans. Yes the old versions can be retrieved by the following way:

- Version id of delete marker found out by

$ aws s3api list-object-versions --bucket izaan-wali1323 --prefix test1.txt --query 'DeleteMarkers[?IsLatest==`true`]'

Then delete marker was deleted using the following command:

$ aws s3api delete-object --bucket izaan-wali1323 --key test1.txt --version-id HnCdaD1LRJJ2PgiSU1WOr2LtGZczntJr

The object test1.txt was restored. Confirmed by the command:

aws s3 ls s3://izaan-wali1323

Q. How would you delete all versions?

Ans. All versions can be deleted by using version id of both latest and previous version.

$ aws s3api delete-object --bucket izaan-wali1323 --key test1.txt --version-id z6lnyVVwfSx7.g5OxVFT9v6mMWI5tY5j

$ aws s3api delete-object --bucket izaan-wali1323 --key test1.txt --version-id .lN08uLeoOlWHXYcAhwFztQXzATRwgDG

### Lab 2.3.3: Tagging S3 Resources

Q. Tag one or more of your objects or buckets using "AWS s3api", or add tags to your bucket through 
CloudFormation. View the tags on them through the CLI or the console.

- using s3Api
- using JSON file
- Cloudformation

Ans: 

### Using s3API

First one object is tagged by "AWS s3api":

$ aws s3api put-object-tagging --bucket izaan-wali1323 --key testorigine.txt --tagging '{"TagSet": [{ "Key": "Originated by", "Value": "Wali" }, { "Key": "Assign
ment", "Value": "AWS Cloudformation 1" }]}'

Then tagging was checked by cli:

$ aws s3api get-object-tagging --bucket izaan-wali1323 --key testorigine.txt

### Using JSON file

Here a Bucket "izaan-wali1318" was tagged using JSON file:

A JSON file "assignment.json" was created with following code:

{

   "TagSet": [

      {

      "Key": "organization",

      "Value": "izaan"

      }

   ]

}

Then the following command executed, and found correct while checking in console:

aws s3api put-bucket-tagging --bucket izaan-wali1318 --tagging file://assignment.json

### Using Cloudformation

Tagging by Cloudformation is added in the next part of the assignment.

Q. Can you change a single tag on a bucket or object, or do you have to change
all its tags at once?

Ans.


### Lab 2.3.1: Object Lifecycles

Q. Create a lifecycle policy for the bucket:
- Move objects to the Infrequent Access class after 30 days.
- Move them to Glacier after 90 days.
- Expire all noncurrent object versions after 7 days.
- Remove all aborted multipart uploads after 1 day.

Ans. A template "s3lifecycletemplate.yaml" was created enabling tagging and lifecycle rule. Then from
the command line the template was validated using the following command:

$ aws cloudformation validate-template --template-body file://s3lifecycletemplate.yaml

After validating the template a stack was created named cfassignment3

$ aws cloudformation create-stack --stack-name cfassignment3 --template-body file://s3lifecycletemplate.yaml

Then it was confirmed from s3 console that the lifecycle rule is enabled for bucket izaan-wali1324

Q. Can you make any of these transitions more quickly?

Ans.

Q. For objects with the tag, you assigned earlier and under the trash/ prefix,
expire them after 1 day.








