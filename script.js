function addPost() {
    let input = document.getElementById("postInput");
    let postList = document.getElementById("post-list");

    if (input.value.trim() === "") {
        alert("내용을 입력해주세요!");
        return;
    }

    let post = document.createElement("div");
    post.className = "post-item";
    post.innerText = input.value;
    postList.prepend(post);

    input.value = ""; // 입력 필드 초기화
}
